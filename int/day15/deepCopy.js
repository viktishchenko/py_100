const object = {
  level1: {
    key1: "Значение 1 уровня",
    level2: {
      key2: "Значение 2 уровня",
      level3: {
        key3: "Значение 3 уровня",
        nestedArray: [
          1,
          2,
          {
            evenDeeper: "Ещё глубже!",
          },
        ],
      },
    },
    anotherKey: "Ещё данные на 1 уровне",
  },
  topLevelKey: "Значение на верхнем уровне",
};

function deepCopy(obj) {
  if (obj instanceof Object) {
    const copy = {};
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        copy[key] = deepCopy(obj[key]);
      }
    }

    // Копируем символьные свойства
    const symbolKeys = Object.getOwnPropertySymbols(obj);
    for (const symKey of symbolKeys) {
      copy[symKey] = deepCopy(obj[symKey]);
    }
    console.log("copy>>", copy);
    return copy;
  }
}

deepCopy(object);
