(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d20fafa"],{b54e:function(t,a,e){"use strict";e.r(a);var l=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-col",{attrs:{justify:"center"}},[e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.getToken}},[t._v(" getToken ")])],1)]),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"user",outlined:""},model:{value:t.user,callback:function(a){t.user=a},expression:"user"}})],1),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"amount",outlined:""},model:{value:t.amount,callback:function(a){t.amount=a},expression:"amount"}})],1)],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.upload}},[t._v(" upload ")])],1)]),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"fileName",outlined:""},model:{value:t.fileName,callback:function(a){t.fileName=a},expression:"fileName"}})],1),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"category",outlined:""},model:{value:t.category,callback:function(a){t.category=a},expression:"category"}})],1),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"price",outlined:""},model:{value:t.price,callback:function(a){t.price=a},expression:"price"}})],1),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"datah",outlined:""},model:{value:t.datah,callback:function(a){t.datah=a},expression:"datah"}})],1)],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.buy}},[t._v(" buy ")])],1)]),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"buyDatah",outlined:""},model:{value:t.buyDatah,callback:function(a){t.buyDatah=a},expression:"buyDatah"}})],1)],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.getInfo}},[t._v(" getInfo ")])],1)])],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.check}},[t._v(" check ")])],1)])],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.confirm}},[t._v(" confirm ")])],1)]),e("v-col",{attrs:{md:"2"}},[e("v-text-field",{attrs:{label:"confirmDatah",outlined:""},model:{value:t.confirmDatah,callback:function(a){t.confirmDatah=a},expression:"confirmDatah"}})],1)],1),e("v-row",[e("v-col",{attrs:{md:"1"}},[e("div",{staticClass:"my-1"},[e("v-btn",{attrs:{large:"",block:""},on:{click:t.test}},[t._v(" test ")])],1)])],1)],1)},o=[],c=e("bc3a"),n=e.n(c),s=(e("6314"),{data:function(){return{user:"0x78658C9AaD8523BB283029C43135CF87339ADC21",amount:"20",fileName:"",category:"",price:"",datah:"",buyDatah:"",confirmDatah:""}},methods:{getToken:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"getToken",user:this.user,token:this.amount}})},upload:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"uploadFile",category:this.category,fileName:this.fileName,price:this.price}})},buy:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"buyFile",dataHash:this.buyDatah}})},getInfo:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"getFileInformation"}})},check:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"checkEvent"}})},confirm:function(){n.a.get("http://141.223.82.142:3000/send",{params:{method:"saleConfirm",dataHash:this.confirmDatah}})},test:function(){window.location.href="http://localhost:8080"}}}),i=s,r=e("2877"),d=e("6544"),u=e.n(d),m=e("8336"),v=e("62ad"),f=e("0fd9"),h=e("8654"),b=Object(r["a"])(i,l,o,!1,null,null,null);a["default"]=b.exports;u()(b,{VBtn:m["a"],VCol:v["a"],VRow:f["a"],VTextField:h["a"]})}}]);
//# sourceMappingURL=chunk-2d20fafa.6ae4c749.js.map