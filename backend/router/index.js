const express = require('express');
const router = express.Router();
const control = require('./control');
const call = require('./call');

router.get('/send', call.sendTransaction);


router.get('/data', control.getData);
router.get('/datainfo', control.getDataInfo);
router.get('/userbalance', control.getUserBalance);
router.get('/userdatainfo', control.getUserDataInfo);

router.post('/data',control.postData);
router.post('/datainfo',control.postDataInfo);

module.exports = router;