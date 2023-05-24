var routeHome = require('./homeRouter');

module.exports = function(app) {
    app.use('/', routeHome);
}

