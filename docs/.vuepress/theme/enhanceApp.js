import { message, Spin } from "ant-design-vue";
import Tabs from "vue-tabs-component";
import VueLazyload from "vue-lazyload";

export default ({
  Vue, // the version of Vue being used in the VuePress app
  options, // the options for the root Vue instance
  router, // the router instance for the app
  siteData, // site metadata
  isServer, // is this enhancement applied in server-rendering or client
}) => {
  // ...apply enhancements to the app
  Vue.config.productionTip = false;
  Vue.prototype.$message = message;
  Vue.use(Spin);
  Vue.use(Tabs);
  Vue.use(VueLazyload, {
    lazyComponent: true,
  });
  // Vue.use(Button);
  // Vue.use(Upload);
  // Vue.use(Icon);
  // Vue.use(Empty);
};
