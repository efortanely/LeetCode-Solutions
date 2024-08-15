function winCondition(senate) {
  let set = new Set(senate);

  if (set.size == 1) {
    return [...set][0];
  } else {
    return false;
  }
}

/**
 * @param {string} senate
 * @return {string}
 */
var predictPartyVictory = function (senate) {
  senate = [...senate];
  let numRadToDelete = 0;
  let numDireToDelete = 0;

  while (!winCondition(senate)) {
    let updatedSenate = [];

    for (let senator of senate) {
      if (senator == "R") {
        if (numRadToDelete > 0) {
          numRadToDelete--;
        } else {
          updatedSenate.push(senator);
          numDireToDelete++;
        }
      } else if (senator == "D") {
        if (numDireToDelete > 0) {
          numDireToDelete--;
        } else {
          updatedSenate.push(senator);
          numRadToDelete++;
        }
      }
    }

    senate = updatedSenate;
  }

  return winCondition(senate) == "R" ? "Radiant" : "Dire";
};

let senate = "RDD";
ans = predictPartyVictory(senate);
console.log(ans);
