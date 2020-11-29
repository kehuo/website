<template>
  <div class="tiobe">
    <a-spin
      size="large"
      tip="Loading..."
      :spinning="chartOptions.series.length<=0"
      style="min-height:80px"
    >
      <div>
        <highcharts v-if="chartOptions.series.length>0" :options="chartOptions"></highcharts>
      </div>
    </a-spin>
    <Content slot-key="between" />
    <a-spin size="large" tip="Loading..." :spinning="!top20.tbody" style="min-height:80px">
      <div class="table-wrapper">
        <table v-if="top20.tbody" class="table-top20">
          <thead v-html="top20.thead"></thead>
          <tbody>
            <tr v-for="(row, index) in top20.tbody" :key="index" @click="onClickTableRow(row.link)">
              <td>{{row.now}}</td>
              <td>{{row.pre}}</td>
              <td>
                <img v-if="row.changeIcon" :src="row.changeIcon" alt="change" />
              </td>
              <td>{{row.name}}</td>
              <td>{{row.rating}}</td>
              <td>{{row.change}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </a-spin>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";
import axios from "axios";
import cheerio from "cheerio";

export default {
  components: {
    highcharts: Chart
  },
  data() {
    return {
      chartOptions: {
        credits: {
          enabled: false
        },
        chart: {
          type: "spline"
        },
        plotOptions: {
          spline: {
            lineWidth: 4,
            states: {
              hover: {
                lineWidth: 5
              }
            },
            marker: {
              enabled: false
            }
          }
        },
        title: {
          text: "TIOBE Programming Community Index",
          x: -20,
          useHTML: true
        },
        subtitle: {
          text: "Source: www.tiobe.com",
          x: -20,
          useHTML: true
        },
        xAxis: {
          type: "datetime",
          dateTimeLabelFormats: {
            year: "%Y"
          }
        },
        yAxis: {
          title: {
            text: "Ratings (%)"
          },
          plotLines: [
            {
              value: 0,
              width: 1,
              color: "#808080"
            }
          ]
        },
        tooltip: {
          valueSuffix: "%",
          dateTimeLabelFormats: {
            week: "%B %Y"
          }
        },
        legend: {
          align: "center",
          borderWidth: 0
        },
        series: []
      },
      top20: {
        thead: null,
        tbody: null
      }
    };
  },
  methods: {
    onClickTableRow(link) {
      window.open("https://www.tiobe.com/tiobe-index/" + link + "/", "_blank");
    }
  },
  beforeMount() {
    // CORS proxy server:
    // https://thingproxy.freeboard.io/fetch/https://www.tiobe.com/tiobe-index/
    axios
      .get("https://cors-anywhere.herokuapp.com/https://www.tiobe.com/tiobe-index/") // To get rid of CORS error
      .then(res => {
        let $ = cheerio.load(res.data);
        // highcharts
        let scripts = $("script").get();
        let testRe = /\$\('#container'\)\.highcharts/;
        let matchRe = /series: (\[\n\s*.*\n\s*\])/;
        for (const script of scripts) {
          if (
            script.children.length === 1 &&
            testRe.test(script.children[0].data)
          ) {
            this.chartOptions.series = eval(
              script.children[0].data.match(matchRe)[1]
            );
            break;
          }
        }

        // table top 20
        let table = $("#top20");
        this.top20.thead = table.find("thead").html();
        let tbody = [];
        for (const tr of table.find("tbody > tr").get()) {
          let row = {
            now: tr.children[0].children[0].data,
            pre: tr.children[1].children[0].data,
            name: tr.children[3].children[0].data,
            rating: tr.children[4].children[0].data,
            change: tr.children[5].children[0].data,
            link: encodeURIComponent(
              tr.children[3].children[0].data
                .replace("/", "-")
                .replace(".", "dot")
                .replace(/\s/g, "-")
                .toLowerCase()
                .replace("#", "sharp")
                .replace(/[+]/g, "plus")
            )
          };
          if (tr.children[2].children.length === 1) {
            row.changeIcon = require("./assets/tiobe/" +
              tr.children[2].children[0].attribs.src.split("/")[2]);
          }
          tbody.push(row);
        }
        this.top20.tbody = tbody;
      })
      .catch(res => {
        console.log(res);
      });
  }
};
</script>

<style lang="scss" scoped>
.tiobe {
  .table-wrapper {
    overflow: scroll;
    &::-webkit-scrollbar {
      display: none;
    }
    -ms-overflow-style: none;
  }

  table.table-top20 {
    text-align: center;

    tbody tr:hover td {
      background-color: lightgrey;
      font-weight: bold;
      cursor: pointer;
    }
  }
}
</style>
