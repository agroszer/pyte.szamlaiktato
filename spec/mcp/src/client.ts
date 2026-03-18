/**
 * OnlineSzámlázó REST API kliens
 * POST JSON hívások a restServer/{methodName} végpontra
 */

export interface ApiConfig {
  apiUrl: string;
  uid: string;
  password: string;
  block: string;
}

export interface ApiResponse {
  status_id: number;
  status: string;
  [key: string]: unknown;
}

export class OnlineSzamlazoClient {
  private config: ApiConfig;

  constructor(config: ApiConfig) {
    this.config = config;
  }

  /**
   * REST API hívás végrehajtása
   * @param method - API metódus neve (pl. "invoiceAdd")
   * @param params - További paraméterek (uid/password/block automatikusan hozzáadódik)
   * @param options - Opcionális beállítások (pl. block nélküli híváshoz)
   */
  async call(
    method: string,
    params: Record<string, unknown> = {},
    options: { skipBlock?: boolean } = {}
  ): Promise<ApiResponse> {
    const url = `${this.config.apiUrl}/${method}`;

    const body: Record<string, unknown> = {
      uid: this.config.uid,
      password: this.config.password,
      ...params,
    };

    if (!options.skipBlock) {
      body.block = params.block ?? this.config.block;
    }

    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = (await response.json()) as ApiResponse;

    if (data.status_id >= 4000) {
      throw new ApiError(method, data);
    }

    return data;
  }
}

export class ApiError extends Error {
  public statusId: number;
  public action: string;
  public response: ApiResponse;

  constructor(action: string, response: ApiResponse) {
    super(`API error ${response.status_id}: ${response.status} (${action})`);
    this.name = "ApiError";
    this.statusId = response.status_id;
    this.action = action;
    this.response = response;
  }
}
