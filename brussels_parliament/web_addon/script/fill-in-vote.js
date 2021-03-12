function fillInWithJson(request, sender, sendResponse) {

  var list = document.getElementsByClassName('has_original dynamic-vote_set');

  if (list) {
    console.log('request', request);
    console.log('list length', list.length);
    // console.log('the long list', list);
    console.log('just one', list[0]);

    // Children of each: 
    // 0 unknow
    // 1 the deputy (o see who they are)
    // 2 the type vote (to change)
    for (let e of list) {
      // the deputy name
      deputy = e.children[1].children[0].children[0].selectedOptions[0].innerText.split(' / ')[0];

      function r(elem) {
        const regexDot = /[.]/gm;
        const regexSpace = /\s/gm;
        let toReturn = elem.replace(regexDot, '').replace(regexSpace, '').toLowerCase();
        return toReturn
      }

      const dataList = request.data;

      let value = 'wait';
      if (dataList.for.find(x => r(x) == r(deputy))) {
        value = 'for';
      } else if (dataList.against.find(x => r(x) == r(deputy))) {
        value = 'against';
      } else if (dataList.abstention.find(x => r(x) == r(deputy))) {
        value = 'abstention';
      } else if (dataList.absent && dataList.absent.find(x => r(x) == r(deputy))) {
        value = 'absent';
      } else {
        console.log('ABSENT', deputy, r(deputy));
        value = 'absent';
      }

      // the value to change
      e.children[2].children[0].value = value;
    }

  }
}

browser.runtime.onMessage.addListener(fillInWithJson);
