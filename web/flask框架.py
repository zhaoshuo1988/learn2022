#导入flask模块
import flask
import 爬虫

#实例化
app = flask.Flask(__name__)
#写API路径
@app.route('/aaa')

#编写视图
def index():
    return flask.render_template('data.html')
@app.route('/api')
def get_data():
    key =flask.request.args.get('key')
    get_value =爬虫.crawl(key)
    print(get_value)
    return flask.jsonify({'data': get_value, 'success' : 0})

    
    
if __name__=='__main__':
    app.run()
