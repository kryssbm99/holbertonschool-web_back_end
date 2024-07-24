const { builtinModules } = require('module');
const reactPlugin = require('eslint-plugin-react');

module.exports = [
  {
    files: ['**/*.js', '**/*.jsx'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...builtinModules.reduce((globals, name) => {
          globals[name] = 'readonly';
          return globals;
        }, {}),
        browser: true,
      },
    },
    plugins: {
      react: reactPlugin,
    },
    rules: {
      'react/react-in-jsx-scope': 'off',
      // Add your custom rules here
    },
  },
];

