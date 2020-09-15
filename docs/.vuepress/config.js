const webpack = require("webpack");
const path = require("path");

module.exports = {
  // configureWebpack: (config, isServer) => {
  //   if (!isServer) {
  //     return {
  //       plugins: [
  //         new webpack.DefinePlugin({
  //           "process.env": {
  //             NODE_ENV: '"production"',
  //             VUE_APP_ML_API_URL: '"http://ziliang.red/ml-api"',
  //             VUE_APP_DEBUG: false,
  //           },
  //         }),
  //       ],
  //     };
  //   }
  // },
  alias: {
    "@assets": path.join(__dirname, "../assets"),
  },
  plugins: [
    ["vuepress-plugin-mathjax", {}],
    [
      "vuepress-plugin-code-copy",
      {
        color: "#757575",
        staticIcon: true,
        selector: 'div[class*="language-"]',
      },
    ],
    ["vuepress-plugin-element-tabs", {}],
    ["check-md", {}],
  ],
  chainWebpack: (config, isServer) => {
    config.module
      .rule("js") // Find the rule.
      .use("babel-loader") // Find the loader
      .tap((options) =>
        Object.assign(options, {
          // Modifying options
          plugins: [
            [
              "import",
              {
                libraryName: "ant-design-vue",
                libraryDirectory: "es",
                style: "css",
              },
            ],
          ],
        })
      );
  },
  markdown: {
    lineNumbers: true,
    extendMarkdown: (md) => {
      md.use(require("markdown-it-footnote"));
      md.use(require("markdown-it-pangu"));
    },
  },
  locales: {
    "/": {
      lang: "en-US",
      title: "Ziliang",
      description: "Not Only a Coder",
    },
    "/zh/": {
      lang: "zh-CN",
      title: "张本人",
      description: "不仅是程序员",
    },
  },
  themeConfig: {
    logo: "/logo.png",
    repo: "LucienZhang/website",
    docsDir: "docs",
    locales: {
      "/": {
        selectText: "Languages",
        label: "English",
        // editLinkText: 'Edit this page on GitHub',
        // serviceWorker: {
        //     updatePopup: {
        //         message: "New content is available.",
        //         buttonText: "Refresh"
        //     }
        // },
        // algolia: {},
        nav: [
          { text: "Programming", link: "/programming/prog-lang/overview" },
          { text: "Machine Learning", link: "/ml/overview" },
          { text: "Misc", link: "/misc/apis" },
        ],
        sidebar: {
          "/programming/": [
            {
              title: "Programming Languages",
              children: [
                ["/programming/prog-lang/overview", "Overview"],
                "/programming/prog-lang/basics",
                "/programming/prog-lang/collections",
                "/programming/prog-lang/controls",
                "/programming/prog-lang/function",
                "/programming/prog-lang/libs",
                "/programming/prog-lang/io",
                "/programming/prog-lang/exceptions",
                "/programming/prog-lang/ood",
                "/programming/prog-lang/scope",
              ],
            },
            {
              title: "Data Structures and Algorithms",
              children: [
                ["/programming/algorithms/overview", "Overview"],
                "/programming/algorithms/math",
                "/programming/algorithms/tree-traversal",
                "/programming/algorithms/balanced-tree",
                "/programming/algorithms/heap",
                "/programming/algorithms/segment-tree",
                "/programming/algorithms/tree-misc",
                "/programming/algorithms/disjoint-sets",
                "/programming/algorithms/graph-traversal",
                "/programming/algorithms/mst",
                "/programming/algorithms/sssp",
                "/programming/algorithms/scc",
                "/programming/algorithms/cut",
                "/programming/algorithms/cache",
                "/programming/algorithms/binary-search",
                "/programming/algorithms/quicksort",
                "/programming/algorithms/knapsack",
                "/programming/algorithms/vertex-cover",
                "/programming/algorithms/set-cover",
                "/programming/algorithms/pca",
                "/programming/algorithms/k-center",
              ],
            },
          ],
          "/ml/": [
            {
              title: "ML & DL",
              children: [["/ml/overview", "Overview"], "/ml/mnist"],
            },
          ],
          "/misc/": [
            {
              title: "Misc",
              children: ["/misc/apis"],
            },
          ],
          // "/projects/": [
          //   "/projects/werewolf",
          //   // {
          //   //     title: 'Games',
          //   //     children: [
          //   //         '/projects/games/werewolf',
          //   //     ]
          //   // },
          // ],
        },
        lastUpdated: "Last Updated",
      },
      "/zh/": {
        selectText: "选择语言",
        label: "简体中文",
        // editLinkText: '在 GitHub 上编辑此页',
        // serviceWorker: {
        //     updatePopup: {
        //         message: "发现新内容可用.",
        //         buttonText: "刷新"
        //     }
        // },
        // algolia: {},
        nav: [
          { text: "编程", link: "/zh/programming/prog-lang/overview" },
          { text: "机器学习", link: "/zh/ml/overview" },
          { text: "杂项", link: "/zh/misc/apis" },
        ],
        sidebar: {
          // "/zh/programming/": [
          //   {
          //     title: "编程语言",
          //     children: [
          //       ["/zh/programming/prog-lang/overview", "概览"],
          //       "/zh/programming/prog-lang/basics",
          //       "/zh/programming/prog-lang/collections",
          //       "/zh/programming/prog-lang/controls",
          //       "/zh/programming/prog-lang/function",
          //       "/zh/programming/prog-lang/libs",
          //       "/zh/programming/prog-lang/io",
          //       "/zh/programming/prog-lang/exceptions",
          //       "/zh/programming/prog-lang/ood",
          //       "/zh/programming/prog-lang/scope",
          //     ],
          //   },
          //   {
          //     title: "算法",
          //     children: [["/zh/programming/algorithms/overview", "概览"], "/zh/programming/algorithms/np-hard/knapsack"],
          //   },
          // ],
          "/zh/ml/": [
            {
              title: "机器学习",
              children: [["/zh/ml/overview", "概览"], "/zh/ml/mnist"],
            },
          ],
          // "/zh/projects/": ["/zh/projects/werewolf"],
        },
        lastUpdated: "上次更新",
      },
    },
  },
};
