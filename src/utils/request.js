import axios from 'axios';

// const api = axios.create({
//   baseURL: 'http://localhost:8000',
// });

// export const request = (url, method, data = {}) => {
//   return api({
//     url,
//     method,
//     data,
//   }).then((res) => res.data);
// };
export const request = (url, method, data = {}) => {
  return new Promise((resolve, reject) => {
    wx.request({
      url: `http://localhost:8000${url}`,
      method: method.toUpperCase(),
      data,
      success: (res) => {
        resolve(res.data);
      },
      fail: (err) => {
        reject(err);
      },
    });
  });
};