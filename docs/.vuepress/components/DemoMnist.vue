<template>
  <div class="mnist">
    <canvas ref="mnist-canvas" id="mnist-canvas"></canvas>
    <div class="container-fluid">
      <div class="row text-center">
        <div class="col-2 col-btn">
          <button class="btn btn-info float-left" @click="clear">Clear</button>
        </div>
        <div class="col-8">
          <div v-if="result!==''">
            <p>Result: {{result}}</p>
            <p>Probability: {{prob}}</p>
          </div>
        </div>
        <div class="col-2 col-btn">
          <button class="btn btn-success float-right" @click="recognize">Recognize</button>
        </div>
      </div>
    </div>
    <!-- <a-upload
      name="image"
      listType="picture-card"
      class="image-uploader"
      :showUploadList="false"
      action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
      :beforeUpload="beforeUpload"
      @change="handleChange"
    >
      <img v-if="imageUrl" :src="imageUrl" alt="Image" />
      <div v-else>
        <a-icon :type="loading ? 'loading' : 'plus'" />
        <div class="ant-upload-text">Upload</div>
      </div>
    </a-upload>
    <hr />-->
  </div>
</template>

<script>
import SignaturePad from "signature_pad";
import mlApi from "../axios-ml";

export default {
  data() {
    return {
      result: "",
      prob: "",
      mnistPad: null
    };
  },
  methods: {
    clear() {
      this.result = "";
      this.prob = "";
      this.mnistPad.clear();
    },
    recognize() {
      if (this.mnistPad.isEmpty()) {
        this.$message.error("Please write down a digit!");
      } else {
        this.getMNISTGridBySize(process.env.VUE_APP_DEBUG, 28, this.img2text);
      }
    },
    getArea() {
      let xs = [];
      let ys = [];

      let orign = this.mnistPad.toData();

      for (let i = 0; i < orign.length; i++) {
        const orignChild = orign[i];

        for (let j = 0; j < orignChild.length; j++) {
          xs.push(orignChild[j].x);
          ys.push(orignChild[j].y);
        }
      }
      let paddingNum = 30;

      let min_x = Math.min.apply(null, xs) - paddingNum;
      let min_y = Math.min.apply(null, ys) - paddingNum;
      let max_x = Math.max.apply(null, xs) + paddingNum;
      let max_y = Math.max.apply(null, ys) + paddingNum;

      let width = max_x - min_x,
        height = max_y - min_y;

      let grid = {
        x: min_x,
        y: min_y,
        w: width,
        h: height
      };

      return grid;
    },
    change2grid(area) {
      let w = area.w,
        h = area.h,
        x = area.x,
        y = area.y;

      let xc = x,
        yc = y,
        wc = w,
        hc = h;

      if (h >= w) {
        xc = x - (h - w) * 0.5;
        wc = h;
      } else {
        yc = y - (w - h) * 0.5;
        hc = w;
      }
      return {
        x: xc,
        y: yc,
        w: wc,
        h: hc
      };
    },
    getMNISTGridBySize(isDev, size, cb) {
      let area = this.getArea();
      let grid = this.change2grid(area);

      if (isDev) {
        this.mnistPad._ctx.strokeStyle = "green";
        this.mnistPad._ctx.strokeRect(area.x, area.y, area.w, area.h);

        this.mnistPad._ctx.strokeStyle = "pink";
        this.mnistPad._ctx.strokeRect(grid.x, grid.y, grid.w, grid.h);
      }
      let canvas = document.createElement("canvas"),
        ctx = canvas.getContext("2d");
      canvas.width = size;
      canvas.height = size;

      let img = new Image();

      img.onload = function() {
        ctx.fillStyle = "white";
        ctx.fillRect(0, 0, grid.w, grid.h);

        ctx.drawImage(img, grid.x, grid.y, grid.w, grid.h, 0, 0, size, size);

        let imgData = ctx.getImageData(0, 0, size, size);

        for (let i = 0; i < imgData.data.length; i += 4) {
          imgData.data[i] = 255 - imgData.data[i];
          imgData.data[i + 1] = 255 - imgData.data[i + 1];
          imgData.data[i + 2] = 255 - imgData.data[i + 2];
          imgData.data[i + 3] = 255;
        }

        ctx.putImageData(imgData, 0, 0);

        cb(canvas.toDataURL());

        if (isDev) {
          document.body.append(canvas);
          setTimeout(function() {
            canvas.remove();
          }, 2000);
        }
      };

      img.src = this.mnistPad.toDataURL();
    },
    img2text(b64img) {
      let formData = new FormData();
      let blob = this.dataURItoBlob(b64img);
      formData.append("predictImg", blob);
      mlApi
        .post("/mnist", formData)
        .then(res => {
          if (res.status != 200) {
            this.$message.error("未知错误");
            console.log(res);
          } else {
            this.result = data.result;
            this.prob = data.prob;
          }
        })
        .catch(res => {
          this.$message.error("未知错误");
          console.log(res);
        });
    },
    dataURItoBlob(dataURI) {
      let byteString;
      if (dataURI.split(",")[0].indexOf("base64") >= 0)
        byteString = atob(dataURI.split(",")[1]);
      else byteString = unescape(dataURI.split(",")[1]);

      let mimeString = dataURI
        .split(",")[0]
        .split(":")[1]
        .split(";")[0];

      let ia = new Uint8Array(byteString.length);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      return new Blob([ia], { type: mimeString });
    }
  },
  mounted() {
    let canvas = this.$refs["mnist-canvas"];
    let mnistPad = new SignaturePad(canvas, {
      backgroundColor: "transparent",
      minWidth: 6,
      maxWidth: 6
    });

    this.mnistPad = mnistPad;

    function resizeCanvas() {
      let ratio = Math.max(window.devicePixelRatio || 1, 1);
      canvas.width = canvas.offsetWidth * ratio;
      canvas.height = canvas.offsetHeight * ratio;
      canvas.getContext("2d").scale(ratio, ratio);
      mnistPad.clear(); // otherwise isEmpty() might return incorrect value
    }
    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();
  }
};
// function getBase64(img, callback) {
//   const reader = new FileReader();
//   reader.addEventListener("load", () => callback(reader.result));
//   reader.readAsDataURL(img);
// }
// export default {
//   data() {
//     return {
//       loading: false,
//       imageUrl: "",
//       resultUrl: ""
//     };
//   },
//   methods: {
//     handleChange(info) {
//       if (info.file.status === "uploading") {
//         this.loading = true;
//         return;
//       }
//       if (info.file.status === "done") {
//         // Get this url from response in real world.
//         getBase64(info.file.originFileObj, imageUrl => {
//           this.imageUrl = imageUrl;
//           this.loading = false;
//         });
//       }
//     },
//     beforeUpload(file) {
//       const isJpgOrPng =
//         file.type === "image/jpeg" || file.type === "image/png";
//       if (!isJpgOrPng) {
//         this.$message.error("You can only upload JPG or PNG file!");
//       }
//       const isLt2M = file.size / 1024 / 1024 < 2;
//       if (!isLt2M) {
//         this.$message.error("Image must be smaller than 2MB!");
//       }
//       return isJpgOrPng && isLt2M;
//     }
//   }
// };
</script>

<style lang="scss">
.mnist {
  #mnist-canvas {
    width: 100%;
    height: 400px;
    max-width: 100%;
    max-height: 100%;
    border: 1px solid #d3d3d3;
  }
  .row {
    height: 55px;
  }
  p {
    margin: 0;
  }
  .col-btn {
    padding: 0;
  }
}
// .result {
//   width: 400px;
//   height: 400px;
//   margin: auto;
//   border: 1px dashed #c3d1dd;
//   display: flex;
//   justify-content: center;
//   align-items: center;

//   img {
//     max-width: 100%;
//   }
// }
// .image-uploader > .ant-upload {
//   width: 400px;
//   height: 400px;
//   margin: auto;
//   float: none;
// }
// .ant-upload-select-picture-card {
//   i {
//     font-size: 32px;
//     color: #999;
//   }

//   .ant-upload-text {
//     margin-top: 8px;
//     color: #666;
//   }
// }
</style>

<style lang="scss">
.ant-message-notice {
  .ant-message-notice-content {
    .anticon {
      vertical-align: 0px;
      top: -1px;
    }
  }
}
</style>
