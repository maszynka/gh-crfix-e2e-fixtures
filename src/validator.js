/**
 * Input validation utilities.
 */

function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function isPositiveNumber(value) {
  return typeof value === 'number' && value > 0;
}

function sanitizeInput(input) {
  if (typeof input !== 'string') return '';
  return input.trim().replace(/[<>]/g, '');
}

function isNonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

module.exports = { isValidEmail, isPositiveNumber, sanitizeInput, isNonEmptyString };
