browser.tabs.executeScript(null, { file: "../script/fill-in-vote.js" });

const data_mock = {
  for: ['Raoul Estassis', 'Norman Michel', 'Prévot Maxime'],
  against: ['Sophie Boonen'],
  abstention: ['Briton Michel'],
  absent: ['Olivier Piedperdu', 'Joëlle Ei']
}

document.getElementById("launch-fillin-vote").addEventListener("click", (e) => {
  var gettingActiveTab = browser.tabs.query({ active: true, currentWindow: true });
  gettingActiveTab.then((tabs) => {
    browser.tabs.sendMessage(tabs[0].id, { data: data_mock });
  });
});

document.getElementById("build-fillin-vote").addEventListener("click", (e) => {
  const data = {
    for: document.getElementById('for').value.split(', '),
    against: document.getElementById('against').value.split(', '),
    abstention: document.getElementById('abstention').value.split(', '),
    absent: document.getElementById('absent').value.split(', ')
  }

  var gettingActiveTab = browser.tabs.query({ active: true, currentWindow: true });
  gettingActiveTab.then((tabs) => {
    browser.tabs.sendMessage(tabs[0].id, { data: data });
  });
});

document.getElementById("build-meli-melo-fillin-vote").addEventListener("click", (e) => {
  const yesRegex = /Ja(\d{1,3})Oui/gm;
  const noRegex = /Neen(\d{1,3})Non/gm;
  const abstentionRegex = /(Onthoudingen|Onthouding)(\d{1,3})(Abstentions|Abstention)/gm;

  // brussels rapport
  // const allRegex = /(Ja(\d{1,3})Oui)|(Neen(\d{1,3})Non)|((Onthoudingen|Onthouding)(\d{1,3})(Abstentions|Abstention))/gm;

  // federal rapport
  const allRegex = /(Oui(\d{1,3})Ja)|(Non(\d{1,3})Nee)|((Abstentions)(\d{1,3})(Onthoudingen))/gm;

  const data = {
    for: document.getElementById('meli-melo').value.replace(allRegex, '!').split('!')[1].split(','),
    against: document.getElementById('meli-melo').value.replace(allRegex, '!').split('!')[2].split(','),
    abstention: document.getElementById('meli-melo').value.replace(allRegex, '!').split('!')[3].split(',')
  }

  var gettingActiveTab = browser.tabs.query({ active: true, currentWindow: true });
  gettingActiveTab.then((tabs) => {
    browser.tabs.sendMessage(tabs[0].id, { data: data });
  });
});