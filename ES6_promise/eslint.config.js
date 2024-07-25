// eslint.config.js

import airbnbBase from 'eslint-config-airbnb-base';
import pluginImport from 'eslint-plugin-import';
import pluginJest from 'eslint-plugin-jest';

export default [
  {
    ignores: ['babel.config.js'],
  },
  {
    files: ['*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
      },
    },
    plugins: {
      import: pluginImport,
      jest: pluginJest,
    },
    rules: {
      ...airbnbBase.rules,
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    settings: {
      jest: {
        version: 26,
      },
    },
  },
];
