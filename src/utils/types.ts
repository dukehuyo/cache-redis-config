export interface RedisConfig {
  host: string;
  port: number;
  username?: string;
  password?: string;
  tls?: boolean;
  db?: number;
  connectTimeout?: number;
  maxRetries?: number;
  retryDelay?: number;
}

export interface CacheConfig {
  defaultTtl: number;
  namespace: string;
  redis: RedisConfig;
}

export type CacheKey = string | number | symbol;

export interface CacheEntry<T> {
  value: T;
  expiresAt: number;
  metadata?: Record<string, unknown>;
}

export interface CacheStats {
  hits: number;
  misses: number;
  expires: number;
  size: number;
}