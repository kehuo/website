const webpack = require("webpack");

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
  plugins: [
    ["vuepress-plugin-mathjax", {}],
    [
      "vuepress-plugin-code-copy",
      {
        color: "#757575",
        staticIcon: true,
      },
    ],
    ["tabs", {}],
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
      title: "Pseudocoder",
      description: "Not Only a Coder",
    },
    "/zh/": {
      lang: "zh-CN",
      title: "张子良的个人站点",
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
          { text: "Projects", link: "/projects/" },
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
              title: "Algorithms",
              children: [["/programming/algorithms/overview", "Overview"], "/programming/algorithms/np-hard/knapsack"],
            },
          ],
          "/ml/": [
            {
              title: "ML & DL",
              children: [["/ml/overview", "Overview"], "/ml/mnist"],
            },
          ],
          "/projects/": [
            "/projects/werewolf",
            // {
            //     title: 'Games',
            //     children: [
            //         '/projects/games/werewolf',
            //     ]
            // },
          ],
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
          { text: "机器学习", link: "/zh/ml/" },
          { text: "其他项目", link: "/zh/projects/" },
        ],
        sidebar: {
          "/zh/ml/": [
            {
              title: "机器学习项目",
              path: "/zh/ml/",
              children: ["/zh/ml/mnist"],
            },
            {
              title: "演示",
              children: ["/zh/ml/demo/mnist"],
            },
          ],
          "/zh/projects/": [
            "/zh/projects/werewolf",
            // {
            //     title: '游戏',
            //     children: [
            //         '/zh/projects/games/werewolf',
            //     ]
            // },
          ],
        },
        lastUpdated: "上次更新",
      },
    },
  },
};
