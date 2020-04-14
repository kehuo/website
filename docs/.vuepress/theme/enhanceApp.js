// import Antd from 'ant-design-vue';
// import { Button } from 'ant-design-vue';
// import 'ant-design-vue/dist/antd.css';
// import DatePicker from 'ant-design-vue/lib/date-picker'; // 加载 JS
// import 'ant-design-vue/lib/date-picker/style/css'; // 加载 CSS
// Vue.use(Button);
import Button from 'ant-design-vue/lib/button';
import 'ant-design-vue/lib/button/style/css';

export default ({
    Vue, // the version of Vue being used in the VuePress app
    options, // the options for the root Vue instance
    router, // the router instance for the app
    siteData, // site metadata
    isServer // is this enhancement applied in server-rendering or client
}) => {
    // ...apply enhancements to the app
    Vue.use(Button);
};
