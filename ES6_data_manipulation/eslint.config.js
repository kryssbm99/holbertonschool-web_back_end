module.exports = [
    {
      files: ["**/*.js"],
      languageOptions: {
        ecmaVersion: 2021,
        sourceType: "module",
        globals: {
          browser: true,
          es2021: true,
        },
      },
      rules: {
        indent: ["error", 2],
        "linebreak-style": ["error", "unix"],
        quotes: ["error", "single"],
        semi: ["error", "always"],
      },
    },
  ];
  