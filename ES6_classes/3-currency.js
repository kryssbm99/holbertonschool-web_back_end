export default class Currency {
    constructor(code, name) {
      this._code = Currency._validateCode(code);
      this._name = Currency._validateName(name);
    }

    get code() {
        return this._code;
      }
    
      set code(newCode) {
        this._code = Currency._validateCode(newCode);
      }

      get name() {
        return this._name;
      }
    
      set name(newName) {
        this._name = Currency._validateName(newName);
      }

      displayFullCurrency() {
        return `${this._name} (${this._code})`;
      }

      static _validateCode(code) {
        if (typeof code !== 'string') {
          throw new TypeError('Code must be a string');
        }
        return code;
      }

      static _validateName(name) {
        if (typeof name !== 'string') {
          throw new TypeError('Name must be a string');
        }
        return name;
      }
    }
    