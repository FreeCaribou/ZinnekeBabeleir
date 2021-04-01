function fillInWithJson(request, sender, sendResponse) {

  var list = document.getElementsByClassName('has_original dynamic-vote_set');

  if (list) {
    console.log('request', request);
    console.log('total deputies votes', request.data.for.length + request.data.against.length + request.data.abstention.length);
    console.log('list length', list.length);
    // console.log('the long list', list);
    console.log('just one', list[0]);

    // Children of each: 
    // 0 unknow
    // 1 the deputy (o see who they are)
    // 2 the type vote (to change)
    for (let e of list) {
      // the deputy name
      // deputy = e.children[1].children[0].children[0].selectedOptions[0].innerText.split(' / ')[0];
      deputy = e.children[1].children[0].innerText.split(' / ')[0];

      function r(elem) {
        const regexDot = /[.]/gm;
        const regexSpace = /\s/gm;
        let toReturn = elem
          .replace(regexDot, '')
          .replace(regexSpace, '')
          .replace('ï', 'i')
          .replace('ö', 'o')
          .replace('Ï', 'I')
          .replace('Ö', 'O')
          .replace('ë', 'e')
          .replace('Ë', 'E')
          .toLowerCase();
        return toReturn
      }

      // The fed rapport give us lastName firstName but we have firstName lastName, so we change our fullname
      function inverseName(fullName) {
        let decomposeName = fullName.split(' ');
        if (decomposeName.length > 1) {
          let firstName = decomposeName[0];
          let returnName = '';
          for (i = 1; i < decomposeName.length; i++) {
            returnName = returnName + decomposeName[i] + ' ';
          }
          returnName = returnName + firstName;
          return returnName;
        } else {
          return fullName;
        }
      }

      const dataList = request.data;

      // console.log('in', inverseName(deputy));

      let value = 'wait';
      if (dataList.for.find(x => r(x) == r(inverseName(deputy)))) {
        value = 'for';
      } else if (dataList.against.find(x => r(x) == r(inverseName(deputy)))) {
        value = 'against';
      } else if (dataList.abstention.find(x => r(x) == r(inverseName(deputy)))) {
        value = 'abstention';
      }
      // else if (dataList.absent && dataList.absent.find(x => r(x) == r(inverseName(deputy)))) {
      //   value = 'absent';
      // }
      else {
        console.log('ABSENT', deputy, r(deputy));
        value = 'absent';
      }

      // the value to change
      e.children[2].children[0].value = value;
    }

  }
}

browser.runtime.onMessage.addListener(fillInWithJson);
