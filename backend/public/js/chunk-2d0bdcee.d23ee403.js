(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0bdcee"],{"2e27":function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-container",[e("v-row",{attrs:{justify:"center"}},[e("v-col",{attrs:{md:"4"}},[e("v-card",{attrs:{outlined:""}},[e("v-card-text",[e("p",{staticClass:"display-1 text--primary"},[t._v(" "+t._s(t.$store.state.productToBuy.name)+" ")]),e("div",[t._v(" Category: "+t._s(t.$store.state.productToBuy.category)+" ")]),e("div",[t._v(" Price: "+t._s(t.$store.state.productToBuy.price)+" ")]),e("div",[t._v(" Uploaded Time: "+t._s(t.$store.state.productToBuy.timestamp)+" ")]),e("div",[t._v(" Seller: "+t._s(t.$store.state.productToBuy.owner)+" ")])]),e("v-card-actions",[e("v-col",{attrs:{md:"2"}},[e("v-btn",{attrs:{large:"",color:"primary"},on:{click:function(a){return t.buyProduct(t.$store.state.productToBuy)}}},[t._v(" Buy ")])],1)],1)],1)],1)],1)],1)},o=[],n=(e("6314"),e("bc3a")),s=e.n(n),c={data:function(){return{}},methods:{buyProduct:function(t){s.a.get("http://141.223.82.142:3000/send",{params:{method:"buyFile",dataHash:t.datahash}}).then((function(){})).catch((function(t){console.log(t)})),alert("거래가 성공적으로 수행되었습니다. 잠시 후 MyPage에서 다운로드가 가능합니다.")}}},d=c,u=e("2877"),i=e("6544"),l=e.n(i),p=e("8336"),v=e("b0af"),y=e("99d9"),_=e("62ad"),f=e("a523"),m=e("0fd9"),b=Object(u["a"])(d,r,o,!1,null,null,null);a["default"]=b.exports;l()(b,{VBtn:p["a"],VCard:v["a"],VCardActions:y["a"],VCardText:y["b"],VCol:_["a"],VContainer:f["a"],VRow:m["a"]})}}]);
//# sourceMappingURL=chunk-2d0bdcee.d23ee403.js.map