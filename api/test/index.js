import request from '@/utils/request'

export function testGet(url) {
  return request({
    url: 'url',
    method: 'get',
  })
}