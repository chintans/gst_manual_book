// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import react from '@astrojs/react';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
    site: 'https://chintans.github.io',
    base: '/gst_manual_book',
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
    }), react(), sitemap()],
});