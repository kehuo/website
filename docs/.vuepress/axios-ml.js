import axios from "axios";

const instance = axios.create({
  baseURL: process.env.VUE_APP_ML_API_URL,
});

instance.defaults.headers.post["Content-Type"] = "multipart/form-data";

if (process.env.VUE_APP_DEBUG) {
  instance.interceptors.request.use((request) => {
    console.log("Starting Request", request);
    return request;
  });

  instance.interceptors.response.use((response) => {
    console.log("Response:", response);
    return response;
  });
}

export default instance;
