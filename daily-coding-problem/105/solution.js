function debounce(callback, wait) {
  console.log('debounce called');
  let timeout;

  return () => {
    // reset setTimeout timer each time function is invoked
    // ensuring it only calls the callback once during the wait time period.
    //  All calls to the parent function will share the timeout variable due to closure
    clearTimeout(timeout);

    timeout = setTimeout(callback, wait);
  };
}

const testCallback = () => {
  console.log('callback was called!');
};

hello = debounce(testCallback, 2000, false);
for (let i = 0; i < 1000; ++i) {
  hello();
}
