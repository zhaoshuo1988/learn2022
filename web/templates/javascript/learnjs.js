var a=123;  // 创建局部变量a,不加var则为全局变量  
a=123;      //创建全局变量  
alert(a) ;  // 弹框显示a的内容
//循环函数
var b=[11,22,33,44]
// 第一种for循环
for (  //小括号写条件
    var i =0; 
    i<4;
    i++){  //{}循环体
    console.log(b[i])
}

for (var item in b){
    console.log(item,b[item]) //日志输出
}

// 普通函数
function func(arg){
    //函数内容
}
function Foo(name,age){   //创建伪类
    this.Name=name;      //伪类属性
    this.Age=age;
    this.Func=function(arg){  //伪类函数
        return this.Name +arg;
    }
}
Foo.prototype={  //伪类原型，类的公共函数
    GetInfo: function(){
        return this.Name
    },
    Funct: function(arg){
        return this.Name+arg;
    }
}

var obj= new Foo('alex',18);  //实例化伪类
var ret = obj.Func('sb');    //使用伪类函数
console.log(ret)
console.log(obj.Funct('年后'))
console.log(obj.GetInfo())

