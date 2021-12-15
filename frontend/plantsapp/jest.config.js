module.exports = {
  //Enable when tests work
  // collectCoverage: true,
  // collectCoverageFrom: ["**/*.{js,vue}", "!**/node_modules/**"],
  moduleFileExtensions: [
    "js",
    "json",
    "vue"
  ],
  transform: {
    '^.+\\.vue$': '@vue/vue3-jest',
    ".*\\.(js)$": 'babel-jest'
  }
}