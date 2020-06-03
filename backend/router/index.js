const express = require('express');
const router = express.Router();
const control = require('./control');
const call = require('./call')

router.get('/send', call.sendTransaction);
router.get('/datainfo', control.getDataInfo);

router.post('/postdata',control.postData);
router.post('/datainfo',control.postDataInfo);

module.exports = router;
