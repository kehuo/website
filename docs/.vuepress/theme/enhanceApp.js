// import Antd from 'ant-design-vue';
// import { Button } from 'ant-design-vue';
// import 'ant-design-vue/dist/antd.css';
// import DatePicker from 'ant-design-vue/lib/date-picker'; // 加载 JS
// import 'ant-design-vue/lib/date-picker/style/css'; // 加载 CSS
// Vue.use(Button);
// 'ant-design-vue/dist/antd.css'
// ant-design-vue/dist/antd.less

import Button from 'ant-design-vue/lib/button';
import 'ant-design-vue/lib/button/style/css';
import Upload from 'ant-design-vue/lib/upload';
import 'ant-design-vue/lib/upload/style/css';
import Icon from 'ant-design-vue/lib/icon';
import 'ant-design-vue/lib/icon/style/css';
import Empty from 'ant-design-vue/lib/empty';
import 'ant-design-vue/lib/empty/style/css';

export default ({
    Vue, // the version of Vue being used in the VuePress app
    options, // the options for the root Vue instance
    router, // the router instance for the app
    siteData, // site metadata
    isServer // is this enhancement applied in server-rendering or client
}) => {
    // ...apply enhancements to the app
    Vue.use(Button);
    Vue.use(Upload);
    Vue.use(Icon);
    Vue.use(Empty);
};
