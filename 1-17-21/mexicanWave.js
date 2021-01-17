function wave(str){
    let waveArr = [];
    for(let i = 0; i < str.length; i++){
      let altStr = str.split('')
      if(altStr[i] != ' '){
        altStr[i] = altStr[i].toUpperCase();
        waveArr.push(altStr.join(''))
      }
    }
    return waveArr;
  }