<template>
  <div class="leetcode">
    <a-spin size="large" tip="Loading..." :spinning="!ranking">
      <p v-if="ranking" id="ranking">{{rankingName}}: {{ranking}}</p>
      <div id="chart">
        <svg />
      </div>
    </a-spin>
  </div>
</template>

<script>
import axios from "axios";
import cheerio from "cheerio";

require("d3");
require("nvd3");

export default {
  props: {
    lang: {
      type: String,
      required: false
    }
  },
  computed: {
    rankingName() {
      return this.lang === "CN" ? "全球排名" : "Global Ranking";
    }
  },
  data() {
    return {
      ranking: null
    };
  },
  mounted() {
    //crawl LeetCode data
    axios
      .get("https://cors-anywhere.herokuapp.com/leetcode.com/lucienzhang/")
      .then(res => {
        let $ = cheerio.load(res.data);
        let panel = $("#base_content ul li").get();
        for (const li of panel) {
          if (li.children[4].data.includes("Global Ranking")) {
            this.ranking = li.children[1].children[0].data.trim();
            break;
          }
        }

        let ranking_data = [{ values: [], key: "Rating", color: "#ff7f0e" }];

        let dataNodeList = $(".puiblic-profile-base").get();
        for (const dataNode of dataNodeList) {
          if (
            dataNode.attribs["ng-controller"] ===
            "PublicProfileController as pc"
          ) {
            let data = JSON.parse(
              "[" + dataNode.attribs["ng-init"].match(/\[\[[^\)]*/)[0] + "]"
            );
            data[0].forEach(function(e, i) {
              ranking_data[0].values.push({
                x: i,
                y: parseInt(e[0]),
                contest_title: data[1][i]
              });
            });
            break;
          }
        }

        nv.addGraph(function() {
          let chart = nv.models
            .lineChart()
            .useInteractiveGuideline(false)
            .margin({ top: 20, right: 20, bottom: 40, left: 55 });

          chart.xAxis.axisLabel("Contest Number");

          chart.yAxis
            .axisLabel("Rating")
            .tickFormat(d3.format(".00f"))
            .axisLabelDistance(-10);

          chart.tooltip.contentGenerator(function(e) {
            return (
              '<div><p style="text-align: left;">' +
              e.point.contest_title +
              '</p></div><div><p style="text-align: left;">' +
              "Rating: " +
              "<strong>" +
              e.point.y +
              "</strong></p></div>"
            );
          });

          d3.select("#chart svg")
            .datum(ranking_data)
            .call(chart);

          //Update the chart when window resizes.
          nv.utils.windowResize(function() {
            chart.update();
          });
          return chart;
        });
      })
      .catch(res => {
        console.log(res);
      });
  }
};
</script>

<style lang="scss" scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.6/nv.d3.min.css");

.leetcode {
  #ranking {
    font-weight: bold;
    font-size: 1.3em;
    color: #5cb85c;
  }

  #chart svg {
    height: 450px;
  }
}
</style>
