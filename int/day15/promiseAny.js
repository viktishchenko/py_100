function promiseAny(promises) {
  return new Promise((resolve, reject) => {
    if (!Array.isArray(promises)) {
      return reject(new TypeError("Argument must be an array"));
    }

    if (promises.length === 0) {
      return reject(new AggregateError([], "All promises were rejected"));
    }

    let rejectedCount = 0;
    const errors = new Array(promises.length);

    promises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((value) => {
          resolve(value); // резолвим с первым успешным результатом
        })
        .catch((error) => {
          errors[index] = error; // сохраняем ошибку в соответствующей позиции
          rejectedCount++;

          if (rejectedCount === promises.length) {
            reject(new AggregateError(errors, "All promises were rejected"));
          }
        });
    });
  });
}

// Пример с успешным выполнением
promiseAny([
  Promise.reject("Error 1"),
  Promise.resolve("Success 1"),
  Promise.resolve("Success 2"),
]).then(console.log); // => "Success 1"

// Пример, когда все промисы отклонены
promiseAny([
  Promise.reject("Error 1"),
  Promise.reject("Error 2"),
  Promise.reject("Error 3"),
]).catch((e) => {
  console.log(e.errors); // => ["Error 1", "Error 2", "Error 3"]
});
