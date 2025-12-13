// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
	integrations: [starlight({
		title: 'GST Manual',
		social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/chintans/gst_manual_book' }],
		sidebar: [
			{
				label: 'Table of Contents',
				link: 'toc',
			},
			{
				label: 'Book',
				autogenerate: { directory: 'gst-manual' },
			},
		],
	}), react()],
});