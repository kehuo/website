module.exports = {
    markdown: {
        lineNumbers: true,
        extendMarkdown: md => {
            md.use(require("markdown-it-footnote"));
        }
    },
    locales: {
        '/': {
            lang: 'en-US',
            title: 'English Title',
            description: 'English Description'
        },
        '/zh/': {
            lang: 'zh-CN',
            title: '中文标题',
            description: '中文描述'
        }
    },
    themeConfig: {
        logo: '/logo.png',
        repo: 'LucienZhang/website',
        docsDir: 'docs',
        locales: {
            '/': {
                selectText: 'Languages',
                label: 'English',
                // editLinkText: 'Edit this page on GitHub',
                // serviceWorker: {
                //     updatePopup: {
                //         message: "New content is available.",
                //         buttonText: "Refresh"
                //     }
                // },
                // algolia: {},
                nav: [
                    { text: 'Machine Learning', link: '/ml/' },
                    { text: 'Projects', link: '/projects/' },
                ],
                // sidebar: 'auto',
                // sidebar: [
                //     ['/ml/', 'ML & DL Applications']
                // ],
                sidebar: {
                    '/ml/': [
                        {
                            title: 'ML & DL Applications',
                            path: '/ml/',
                            children: [
                                '/ml/mnist',
                            ]
                        },
                        {
                            title: 'Demo',
                            children: [
                                '/ml/demo/mnist',
                            ]
                        }
                    ],
                    '/projects/': [
                        '/projects/werewolf',
                        // {
                        //     title: 'Games',
                        //     children: [
                        //         '/projects/games/werewolf',
                        //     ]
                        // },
                    ]
                },
                lastUpdated: 'Last Updated',
                // sidebar: {
                //     '/': [/* ... */],
                //     '/ml/': [/* ... */],
                //     '/games/': [/* ... */],
                // }
            },
            '/zh/': {
                selectText: '选择语言',
                label: '简体中文',
                // editLinkText: '在 GitHub 上编辑此页',
                // serviceWorker: {
                //     updatePopup: {
                //         message: "发现新内容可用.",
                //         buttonText: "刷新"
                //     }
                // },
                // algolia: {},
                nav: [
                    { text: '机器学习', link: '/zh/ml/' },
                    { text: '其他项目', link: '/zh/projects/' },
                ],
                sidebar: {
                    '/zh/ml/': [
                        {
                            title: '机器学习项目',
                            path: '/zh/ml/',
                            children: [
                                '/zh/ml/mnist',
                            ]
                        },
                        {
                            title: '演示',
                            children: [
                                '/zh/ml/demo/mnist',
                            ]
                        }
                    ],
                    '/zh/projects/': [
                        '/zh/projects/werewolf',
                        // {
                        //     title: '游戏',
                        //     children: [
                        //         '/zh/projects/games/werewolf',
                        //     ]
                        // },
                    ]
                },
                lastUpdated: '上次更新',
            }
        }
    }
};
