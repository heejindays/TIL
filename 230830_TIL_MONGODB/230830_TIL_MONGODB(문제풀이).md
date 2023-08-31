## MongoDB (문제 풀이)

// update document
db.inventory.insertMany( [
	{ item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" },
	{ item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },	
	{ item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },
	{ item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" },
	{ item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
	{ item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
	{ item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
	{ item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
	{ item: "sketchbook", qty: 80, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
	{ item: "sketch pad", qty: 95, size: { h: 22.85, w: 30.5, uom: "cm" }, status: "A" }
] );



**위 collection을 활용해서 아래 문제를 풀어보자!**

<br>

**// _id만 빼고 전체 출력**

db.inventory.find( { }, { _id: 0 } )



<br>

**// status가 D인 document**

db.inventory.find( { status:'D' } )



<br>

**// qty가 높은 순부터 (내림차순)**

db.inventory.find().sort( { qty:-1 } )



<br>

**// qty가 80 미만인 document를 낮은 순부터 (오름차순)**

db.inventory.find( { qty : { $lt:80 } } ).sort( { qty:1 } )



<br>

**// qty가 75보다 크거나 같고, 100보다 작은 document**

db.inventory.find( { $and: [ { qty: { $gte:75 } }, { qty: { $lt:100 } } ] } )



<br>

**// qty가 60이상이면서 size의 h가 10 이상인 document**

db.inventory.find( { $and: [ { qty: { $gte: 60 } }, {"size.h": { $gte: 10 } } ] } )



<br>

**// uom이 in인 document**

db.inventory.find( { "size.uom" : 'in' } )



<br>

**// item이 p로 시작하는 document**

db.inventory.find({ item: { $regex: '^p' } })



<br>

**// item이 r로 끝나는 document**

db.inventory.find({ item: { $regex: 'r$' } })



<br>

**// item에 r이 들어간 document**

db.inventory.find({ item: {$regex:'r'} })



<br>

**// qty의 값이 25나 45인 document**

db.inventory.find( {$or: [{qty:25}, {qty:45}] } )



<br>

**// w의 값이 11나 21가 아닌 documnet**

db.inventory.find( {$nor: [{ "size.w":11 }, { "size.w":21 }] } )



<br>

**// $eq를 이용하여 item이 'notebook'인 document를 찾아, item과 status만 출력**

db.inventory.find( {item: {$eq: 'notebook'}}, {item: 1, status: 1, _id: 0} )



<br>

**// status가 A이거나 qty가 30미만 인 document**

db.inventory.find({ $or : [ {status:'A'}, {qty:{$lt:30}} ]})



<br>

**// status가 A이고 qty가 30미만 인 document**

db.inventory.find({ $and : [ {status:'A'}, {qty:{$lt:30}} ]})



<br>

**// h 기준으로 오름차순 정렬**

db.inventory.find().sort({"size.h":1})



<br>

**// h가 10보다 큰 document**

db.inventory.find({ "size.h": {$gt:10}})



<br>

**// qty가 100이 아닌 document 출력**

db.inventory.find({ qty: { $ne:100 } })



<br>

**// qty가 존재하면서, qty의 값이 50보다 큰 document**

db.inventory.find( $and : [{qty: {$exists: true}}, {qty: {$gt:50}} ])



<br>

**// uom이 cm인 document들의 item과 status만 출력**

db.inventory.find({ "size.uom": "cm" }, { item: 1, status: 1, _id: 0 })



<br>

**// item 중에서 's'로 시작하는 document를 찾아, item과 status만 출력하기**

db.inventory.find( {item: { $regex: '^s' }}, {item: 1, status: 1, _id: 0})



<br>

**// status가 'A'또는 'D'인 document 출력하기**

db.inventory.find( {$or : [{status:'A'}, {status:'D'}]} )



<br>

**// qty가 50 이상이면서 size의 w가 20이상인 document 출력하기**

db.inventory.find( {$and : [{qty: {$gte: 50}}, {"size.w":{$gte:20}} ]} )



<br>

**// size의 h가 10이 아닌 document 출력하기**

db.inventory.find( {"size.h" : {$ne:10}} )



<br>

**// qty가 80 미만이면서 status가 'A'인 document만 출력하기**

db.inventory.find({ $and: [ {qty:{$lt:80}}, {status:'A'} ] })



<br>

**// w 기준으로 오름차순 정렬해서 document 출력하기**

db.inventory.find().sort({"size.w":1})



<br>

**// item 스펠링이 6글자 이상인 document를 qty 내림차순으로 출력하기**

db.inventory.find({ $expr: { $gte: [ { $strLenCP: "$item" }, 6 ] } }).sort({ qty: -1 })



<br>

**// size의 w 값이 11나 35.5가 아닌 documnet 중에서 id 빼고 출력하기**

db.inventory.find( {$nor : [{"size.w": 11}, {"size.w":35.5}]}, {item: 1, status: 1, _id: 0})