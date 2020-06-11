const webpack = require("webpack");

module.exports = {
  configureWebpack: (config, isServer) => {
    if (!isServer) {
      return {
        plugins: [
          new webpack.DefinePlugin({
            "process.env": {
              NODE_ENV: '"production"',
              VUE_APP_ML_API_URL: '"http://ziliang.red/ml-api"',
              VUE_APP_DEBUG: false,
            },
          }),
        ],
      };
    }
  },
  plugins: [
    ["vuepress-plugin-mathjax", {}],
    [
      "vuepress-plugin-code-copy",
      {
        color: "#ffffff",
        staticIcon: true,
      },
    ],
    ["tabs", {}],
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
          { text: "Machine Learning", link: "/ml/" },
          { text: "Projects", link: "/projects/" },
          { text: "Algorithms", link: "/algorithms/" },
        ],
        // sidebar: 'auto',
        // sidebar: [
        //     ['/ml/', 'ML & DL Applications']
        // ],
        sidebar: {
          "/ml/": [
            {
              title: "ML & DL Applications",
              path: "/ml/",
              children: ["/ml/mnist"],
            },
            {
              title: "Demo",
              children: ["/ml/demo/mnist"],
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
          "/algorithms/": [
            {
              title: "NP-Hard",
              path: "/algorithms/np-hard/",
              children: ["/algorithms/np-hard/knapsack"],
            },
          ],
        },
        lastUpdated: "Last Updated",
        // sidebar: {
        //     '/': [/* ... */],
        //     '/ml/': [/* ... */],
        //     '/games/': [/* ... */],
        // }
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
