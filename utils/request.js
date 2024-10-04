import config from '@/config'

// const service = axios.create({
// 	baseURL: 'https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant',
// 	timeout: 6000,
// 	crossDomain: true
// })

let timeout = 10000
const baseUrl = config.baseUrl

const request = config => {
  return new Promise((resolve, reject) => {
    uni.request({
        method: config.method || 'get',
        timeout: config.timeout ||  timeout,
        url: config.baseUrl || baseUrl + config.url,
        data: config.data,
        header: config.header,
        dataType: 'json'
      }).then(response => {
        let [error, res] = response
        if (error) {
          toast('后端接口连接异常')
          reject('后端接口连接异常')
          return
        }
        const msg = errorCode[code] || res.data.msg || errorCode['default']
        resolve(res.data)
      })
      .catch(error => {
        let { message } = error
        if (message === 'Network Error') {
          message = '后端接口连接异常'
        } else if (message.includes('timeout')) {
          message = '系统接口请求超时'
        } else if (message.includes('Request failed with status code')) {
          message = '系统接口' + message.substr(message.length - 3) + '异常'
        }
        toast(message)
        reject(error)
      })
  })
}

export default request
