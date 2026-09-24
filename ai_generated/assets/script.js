/* ===== پایتون برای علم داده — منطق مشترک همه‌ی بخش‌ها ===== */

/* اجرای فوری قبل از رندر، برای جلوگیری از پرش رنگ تم */
(function () {
  try {
    var saved = localStorage.getItem('py-course-theme');
    var theme = saved || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
  } catch (e) {
    document.documentElement.setAttribute('data-theme', 'light');
  }
})();

document.addEventListener('DOMContentLoaded', function () {

  /* دکمه‌ی سوییچ تم */
  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('py-course-theme', next); } catch (e) {}
    });
  }

  /* افکت تایپ‌شوندن کد در سلول‌های نمونه (هر سلول با data-animate) */
  var reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.code-cell[data-animate]').forEach(function (cell) {
    var codeEl = cell.querySelector('.code');
    var outEl = cell.querySelector('.cell-out');
    if (!codeEl) return;
    var full = codeEl.textContent;

    if (reduceMotion) {
      if (outEl) outEl.hidden = false;
      return;
    }

    codeEl.textContent = '';
    var i = 0;
    function tick() {
      if (i <= full.length) {
        codeEl.textContent = full.slice(0, i);
        i++;
        setTimeout(tick, 24);
      } else if (outEl) {
        outEl.hidden = false;
      }
    }
    setTimeout(tick, 400);
  });
});
