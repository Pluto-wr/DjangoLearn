const fs = require('fs');
const ini =require('ini');

const express = require('express')
const app = express()
let port = 10000
app.get('/', (req, res) => {
  res.send('Hello World!')
})
const common = ini.parse(fs.readFileSync("common.ini","utf-8"));
port = common.common.port
app.get('/index',(req,res)=>{
  //请求的路由地址
		fs.readFile("index.html",function(err,data){
      res.setHeader('Content-Type', 'text/html');
			//设置响应头
			//加载的数据结束
			res.end(data)
		})
})
app.get('/home',(req,res)=>{
  //请求的路由地址
                fs.readFile("index.html",function(err,data){
      res.setHeader('Content-Type', 'text/html');
                        //设置响应头
                        //加载的数据结束
                        res.end(data)
                })
})
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

