/**
 * Session szintű in-memory cache
 * Az MCP szerver életciklusáig él (amíg a Claude Code session tart)
 */

interface CacheEntry<T> {
  data: T;
  expiresAt: number;
}

export class SessionCache {
  private store = new Map<string, CacheEntry<unknown>>();
  private defaultTtlMs: number;

  constructor(defaultTtlMinutes: number = 30) {
    this.defaultTtlMs = defaultTtlMinutes * 60 * 1000;
  }

  get<T>(key: string): T | null {
    const entry = this.store.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiresAt) {
      this.store.delete(key);
      return null;
    }
    return entry.data as T;
  }

  set<T>(key: string, data: T, ttlMinutes?: number): void {
    const ttlMs = ttlMinutes ? ttlMinutes * 60 * 1000 : this.defaultTtlMs;
    this.store.set(key, {
      data,
      expiresAt: Date.now() + ttlMs,
    });
  }

  invalidate(key: string): void {
    this.store.delete(key);
  }

  /** Adott prefixszel kezdődő kulcsok törlése */
  invalidatePrefix(prefix: string): void {
    for (const key of this.store.keys()) {
      if (key.startsWith(prefix)) {
        this.store.delete(key);
      }
    }
  }

  clear(): void {
    this.store.clear();
  }
}
