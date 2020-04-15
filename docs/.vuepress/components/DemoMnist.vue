<template>
  <div>
    <a-upload
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
    <hr />
    <div class="result">
      <img v-if="resultUrl" :src="resultUrl" alt="Result" />
      <a-empty v-else description="Result" />
    </div>
  </div>
</template>

<script>
function getBase64(img, callback) {
  const reader = new FileReader();
  reader.addEventListener("load", () => callback(reader.result));
  reader.readAsDataURL(img);
}
export default {
  data() {
    return {
      loading: false,
      imageUrl: "",
      resultUrl: ""
    };
  },
  methods: {
    handleChange(info) {
      if (info.file.status === "uploading") {
        this.loading = true;
        return;
      }
      if (info.file.status === "done") {
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, imageUrl => {
          this.imageUrl = imageUrl;
          this.loading = false;
        });
      }
    },
    beforeUpload(file) {
      const isJpgOrPng =
        file.type === "image/jpeg" || file.type === "image/png";
      if (!isJpgOrPng) {
        this.$message.error("You can only upload JPG or PNG file!");
      }
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        this.$message.error("Image must be smaller than 2MB!");
      }
      return isJpgOrPng && isLt2M;
    }
  }
};
</script>

<style lang="scss">
.result {
  width: 400px;
  height: 400px;
  margin: auto;
  border: 1px dashed #c3d1dd;
  display: flex;
  justify-content: center;
  align-items: center;

  img {
    max-width: 100%;
  }
}
.image-uploader > .ant-upload {
  width: 400px;
  height: 400px;
  margin: auto;
  float: none;
}
.ant-upload-select-picture-card {
  i {
    font-size: 32px;
    color: #999;
  }

  .ant-upload-text {
    margin-top: 8px;
    color: #666;
  }
}
</style>
