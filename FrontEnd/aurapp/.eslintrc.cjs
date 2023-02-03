module.exports = {
	// ...
	extends: ['standard', 'plugin:astro/recommended'],
	rules: {
		'no-tabs': 'off',
		indent: 'off',
		'space-before-function-paren': 'off'
	},
	// ...
	overrides: [
		{
			parser: 'astro-eslint-parser',
			parserOptions: {
				parser: '@typescript-eslint/parser',
			},
			rules: {}
		}
	]
}