var express = require('express');
var router = express.Router();
var controller = require('../controllers/homeController');

router.get('/', controller.home);
router.post('/', controller.homePost);

module.exports = router;