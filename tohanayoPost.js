var path = require('path');
var fs = require('fs');
var articlePath = path.resolve(__dirname, './article');
fs.readdir(articlePath, function(err, files) {
  if (err) throw err;

  files.map(function(file) {
    fs.readFile(path.join(articlePath, file), {encoding: 'utf-8'}, function(err, data) {
      if (err) throw err;
      console.log('read', path.join(articlePath, file));
      var datalines = data.split("\n");
      datalines[0] = '---\ntitle: ' + datalines[0];
      var tags = datalines[1].split(' ');
      datalines[1] = 'tags:';
      tags.map(function(tag) {
        datalines[1] += '\n\t-' + tag;
      });
      datalines[1] += '\nauthor: disoul\n---';
      fs.writeFile(
          path.join(articlePath, file), 
          datalines.join("\n"), 
          function(err) {
            if (err) throw err;
            console.log('write', file);    
          }
      );
    });
  });
});
