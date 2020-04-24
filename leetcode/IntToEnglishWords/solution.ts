/**
 * @param {number} num
 * @return {string}
 */

function twoDigitsLessThan20(num: number) {
  const switcher = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
  };
  return switcher[num];
}

function ten(num: number): string {
  const switcher = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
  };
  return switcher[num];
}

function oneDigit(num: number): string {
  const switcher = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
  };
  return switcher[num];
}

function twoDigits(num: number): string {
  if (!num) {
    return '';
  } else if (num < 10) {
    return oneDigit(num);
  } else if (num < 20) {
    return twoDigitsLessThan20(num);
  } else {
    const tens: number = Math.floor(num / 10);
    const rest: number = num - tens * 10;
    return rest ? ten(tens) + ' ' + oneDigit(rest) : ten(tens);
  }
}

function threeDigits(num: number): string {
  const hundred: number = Math.floor(num / 100);
  const rest: number = num - hundred * 100;

  if (hundred && rest) {
    return oneDigit(hundred) + ' Hundred ' + twoDigits(rest);
  } else if (!hundred && rest) {
    return twoDigits(rest);
  } else if (hundred && !rest) {
    return oneDigit(hundred) + ' Hundred';
  }
}

var numberToWords = function (num: number): string {
  if (!num) {
    return 'Zero';
  }

  const billion: number = Math.floor(num / 1000000000);
  const million: number = Math.floor((num - billion * 1000000000) / 1000000);
  const thousand: number = Math.floor(
    (num - billion * 1000000000 - million * 1000000) / 1000
  );
  const rest: number =
    num - billion * 1000000000 - million * 1000000 - thousand * 1000;

  let result: string = '';

  if (billion) {
    result += threeDigits(billion) + ' Billion';
  }
  if (million) {
    result += result ? ' ' : '';
    result += threeDigits(million) + ' Million';
  }
  if (thousand) {
    result += result ? ' ' : '';
    result += threeDigits(thousand) + ' Thousand';
  }
  if (rest) {
    result += result ? ' ' : '';
    result += threeDigits(rest);
  }

  return result;
};
