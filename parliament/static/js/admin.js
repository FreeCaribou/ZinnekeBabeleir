console.log('hello admin');

document.addEventListener('DOMContentLoaded', function () {
  var textarea = document.getElementById('id_detail');
  sceditor.create(textarea, {
    format: 'bbcode',
    style: 'https://cdn.jsdelivr.net/npm/sceditor@3/minified/themes/content/default.min.css'
  });
}, false);
