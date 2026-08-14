// ── Types ──

export interface Source {
  key: string;
  name: string;
  home_url: string;
}

export interface Post {
  title: string;
  date: string;
  slug: string;
  source: string;
  source_name: string;
  home_url: string;
  has_translation: boolean;
  has_summary: boolean;
  orig_file: string;
  zh_file: string;
}

export interface PostContent {
  slug: string;
  title: string;
  content: string;
  source: string;
  source_name: string;
  has_translation: boolean;
}

export interface BilingualContent {
  slug: string;
  title: string;
  orig: string;
  zh: string | null;
  source: string;
  source_name: string;
  has_translation: boolean;
}

export interface SummaryResult {
  slug: string;
  summary: string | null;
  cached: boolean;
}

// ── API ──

const BASE = '/api';

export async function fetchSources(): Promise<Source[]> {
  const res = await fetch(`${BASE}/sources`);
  return res.json();
}

export async function fetchPosts(source?: string, search?: string): Promise<Post[]> {
  const params = new URLSearchParams();
  if (source && source !== 'all') params.set('source', source);
  if (search) params.set('search', search);
  const url = `${BASE}/posts${params.toString() ? '?' + params.toString() : ''}`;
  const res = await fetch(url);
  return res.ok ? res.json() : [];
}

export async function fetchPostContent(slug: string, lang: string): Promise<PostContent> {
  const res = await fetch(`${BASE}/posts/${slug}?lang=${lang}`);
  return res.json();
}

export async function fetchBilingualContent(slug: string): Promise<BilingualContent> {
  const res = await fetch(`${BASE}/posts/${slug}/bilingual`);
  return res.json();
}

export async function fetchSummary(slug: string): Promise<SummaryResult> {
  const res = await fetch(`${BASE}/posts/${slug}/summary`);
  return res.json();
}

export async function generateSummary(slug: string): Promise<SummaryResult> {
  const res = await fetch(`${BASE}/posts/${slug}/summary`, { method: 'POST' });
  return res.json();
}

export async function triggerFetch(source: string, days: number): Promise<{ status: string; message: string }> {
  const res = await fetch(`${BASE}/fetch/${source}?days=${days}`, { method: 'POST' });
  return res.json();
}

export async function triggerTranslate(slug: string): Promise<{ status: string; message: string }> {
  const res = await fetch(`${BASE}/translate/${slug}`, { method: 'POST' });
  return res.json();
}
