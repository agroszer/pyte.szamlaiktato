from typing import Any, Optional
from dataclasses import dataclass, asdict
from .client import OnlineSzamlazoClient


@dataclass
class InstallRequest:
    user: str
    service_key: str
    block_name: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    tax_number: str
    bank_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    email: str
    invoice_issue: int
    restart_number_by_year: int
    street_number: Optional[str] = None
    door: Optional[str] = None
    eu_tax_number: Optional[str] = None
    telephone: Optional[str] = None
    comment: Optional[str] = None
    lang: Optional[str] = None
    logo: Optional[Any] = None
    invoice_template: Optional[str] = None
    invoice_number_format: Optional[str] = None
    currency: Optional[str] = None
    installType: Optional[str] = None
    other: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    admin_user_type: Optional[int] = None


@dataclass
class InstallResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    other: Optional[str] = None


@dataclass
class UpdateRequest:
    user: str
    block_name: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    tax_number: str
    bank_name: str
    bank_number: str
    email: str
    invoice_issue: int
    restart_number_by_year: int
    street_number: Optional[str] = None
    door: Optional[str] = None
    eu_tax_number: Optional[str] = None
    telephone: Optional[str] = None
    comment: Optional[str] = None
    lang: Optional[str] = None
    logo: Optional[Any] = None
    invoice_template: Optional[str] = None
    other: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    admin_user_type: Optional[int] = None


@dataclass
class UpdateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    other: Optional[str] = None


@dataclass
class CustomerAddRequest:
    instance_id: str
    sid: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    email: str
    invoice_send: int
    active: int
    lang: str
    legal_status: int
    region: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    firm_type: Optional[int] = None
    other: Optional[str] = None


@dataclass
class CustomerAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerModifyRequest:
    instance_id: str
    sid: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    active: int
    lang: str
    firm_type: int
    legal_status: str
    region: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    other: Optional[str] = None


@dataclass
class CustomerModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerGetRequest:
    instance_id: str
    sid: str
    tax_number: Optional[str] = None
    email: Optional[str] = None


@dataclass
class CustomerGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    active: Optional[int] = None
    lang: Optional[str] = None
    firm_type: Optional[int] = None
    legal_status: Optional[str] = None
    date: Optional[str] = None
    users_id: Optional[int] = None
    master_customer_sid: Optional[str] = None
    modify_date: Optional[str] = None
    other_json: Optional[str] = None


@dataclass
class CustomerActivateRequest:
    instance_id: str
    sid: str


@dataclass
class CustomerActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerInactivateRequest:
    instance_id: str
    sid: str


@dataclass
class CustomerInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerSwapRequest:
    instance_id: str
    sid: str
    swapped_sids: list[dict[str, Any]]


@dataclass
class CustomerSwapResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerListRequest:
    instance_id: str
    firm_type: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None


@dataclass
class CustomerListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    customers: Optional[list[dict[str, Any]]] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank: Optional[str] = None
    active: Optional[int] = None
    lang: Optional[str] = None
    legal_status: Optional[str] = None
    date: Optional[str] = None
    users_id: Optional[int] = None
    other_json: Optional[str] = None
    modify_date: Optional[str] = None


@dataclass
class ProductAddRequest:
    instance_id: str
    sid: str
    name: str
    net_price_single: float
    tax_code: str
    currency: str
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    lang: Optional[list[dict[str, Any]]] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    lineNatureIndicator: Optional[str] = None
    FINAL_DATADELETE_CODE_SET: Optional[int] = None
    intermediatedService: Optional[int] = None


@dataclass
class ProductAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductModifyRequest:
    instance_id: str
    sid: str
    name: str
    net_price_single: float
    tax_code: str
    currency: str
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    lang: Optional[list[dict[str, Any]]] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    lineNatureIndicator: Optional[str] = None
    FINAL_DATADELETE_CODE_SET: Optional[int] = None
    intermediatedService: Optional[int] = None


@dataclass
class ProductModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductGetRequest:
    instance_id: str
    sid: str


@dataclass
class ProductGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[str] = None
    currency: Optional[str] = None
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    active: Optional[int] = None
    date: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    tax_code: Optional[str] = None
    lang: Optional[list[dict[str, Any]]] = None
    files_number: Optional[int] = None
    modify_date: Optional[str] = None


@dataclass
class ProductActivateRequest:
    instance_id: str
    sid: str


@dataclass
class ProductActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductInactivateRequest:
    instance_id: str
    sid: str


@dataclass
class ProductInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductListRequest:
    instance_id: str
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    active: Optional[int] = None
    currency: Optional[str] = None
    lang: Optional[str] = None
    name: Optional[str] = None
    sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None


@dataclass
class ProductListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    service_id: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    tax_categories_id: Optional[int] = None
    tax_code: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_type_id: Optional[int] = None
    cost_centre: Optional[str] = None
    cost_centre_id: Optional[int] = None
    active: Optional[int] = None
    date: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    orderby: Optional[int] = None
    files_number: Optional[int] = None
    modify_date: Optional[str] = None


@dataclass
class ProductFileListRequest:
    instance_id: str
    sid: str
    with_file_content: bool


@dataclass
class ProductFileListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    sid: Optional[str] = None
    filename: Optional[str] = None
    checksum: Optional[str] = None
    file_type: Optional[str] = None
    file: Optional[str] = None


@dataclass
class OuterDatasourcesRequest:
    instance_id: str


@dataclass
class OuterDatasourcesResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    settings: Optional[str] = None


@dataclass
class OuterDatasourcesGetRequest:
    instance_id: str
    type_: str


@dataclass
class OuterDatasourcesGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    data: Optional[str] = None


@dataclass
class OuterDatasourcesSaveRequest:
    instance_id: str
    type_: str
    data: str
    nav_xml_user: str
    nav_xml_password: str
    nav_xml_key: str
    nav_xml_exchange_key: str
    nav_invoice_download: int


@dataclass
class OuterDatasourcesSaveResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class AdminUserAddRequest:
    instance_id: str
    name: str
    email: str
    mailsend: bool
    groups_id: int
    user_type: int
    service_key: Optional[str] = None


@dataclass
class AdminUserAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


@dataclass
class AdminUserPasswordRequest:
    instance_id: str
    email: str
    new_password: str


@dataclass
class AdminUserPasswordResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class AdminUserDelRequest:
    instance_id: str
    email: str


@dataclass
class AdminUserDelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class BlockAddRequest:
    instance_id: str
    block_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    invoice_issue: int
    email: str
    restart_number_by_year: int
    lang: str
    invoice_template: str
    currency: str
    other: list[dict[str, Any]]
    countryMustVisibleInInvoice: int
    bank_name: Optional[str] = None
    comment: Optional[str] = None
    logo: Optional[int] = None
    invoice_number_format: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    certificate_logo_visible: Optional[int] = None
    order_number_visible: Optional[int] = None
    pdfConvertZpl: Optional[int] = None
    pdfConvertZplDownload: Optional[int] = None
    pdf_design05: Optional[list[dict[str, Any]]] = None
    color1: Optional[str] = None


@dataclass
class BlockAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    block_id: Optional[int] = None
    block: Optional[str] = None


@dataclass
class BlockUpdateCompanyDataRequest:
    instance_id: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    street_number: str
    door: str
    tax_number: str
    eu_tax_number: str


@dataclass
class BlockUpdateCompanyDataResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class BlockModifyRequest:
    instance_id: str
    block_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    invoice_issue: int
    email: str
    restart_number_by_year: int
    lang: str
    invoice_template: str
    currency: str
    other: list[dict[str, Any]]
    countryMustVisibleInInvoice: int
    bank_name: Optional[str] = None
    comment: Optional[str] = None
    logo: Optional[int] = None
    invoice_number_format: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    certificate_logo_visible: Optional[int] = None
    order_number_visible: Optional[int] = None
    pdfConvertZpl: Optional[int] = None
    pdfConvertZplDownload: Optional[int] = None
    pdf_design05: Optional[list[dict[str, Any]]] = None
    color1: Optional[str] = None


@dataclass
class BlockModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    block_id: Optional[int] = None
    block: Optional[str] = None


@dataclass
class BlockListRequest:
    instance_id: str
    active: int


@dataclass
class BlockListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    block_name: Optional[str] = None
    name: Optional[str] = None
    lang: Optional[str] = None
    currency: Optional[str] = None
    invoice_number_pre: Optional[str] = None
    active: Optional[int] = None


@dataclass
class BlockCloseRequest:
    instance_id: str
    block_id: int
    block_name: str


@dataclass
class BlockCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class BlockOpenRequest:
    instance_id: str
    block_id: int
    block_name: str


@dataclass
class BlockOpenResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class CostCentreAddRequest:
    instance_id: str
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostCentreAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreModifyRequest:
    instance_id: str
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostCentreModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreListRequest:
    instance_id: str


@dataclass
class CostCentreListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    cost_centres: Optional[list[dict[str, Any]]] = None
    name: Optional[str] = None
    code: Optional[str] = None
    comment: Optional[int] = None


@dataclass
class CostCentreActivateRequest:
    instance_id: str
    code: str


@dataclass
class CostCentreActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreInactivateRequest:
    instance_id: str
    code: str


@dataclass
class CostCentreInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeAddRequest:
    instance_id: str
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostTypeAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeModifyRequest:
    instance_id: str
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostTypeModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeListRequest:
    instance_id: str


@dataclass
class CostTypeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None
    active: Optional[int] = None


@dataclass
class CostTypeActivateRequest:
    instance_id: str
    code: str


@dataclass
class CostTypeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeInactivateRequest:
    instance_id: str
    code: str


@dataclass
class CostTypeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectListRequest:
    instance_id: Optional[str] = None
    active: Optional[int] = None


@dataclass
class ProjectListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    projects: Optional[list[dict[str, Any]]] = None


@dataclass
class ProjectGetRequest:
    code: str
    instance_id: Optional[str] = None


@dataclass
class ProjectGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id_: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    is_booking: Optional[int] = None


@dataclass
class ProjectCreateRequest:
    code: str
    name: str
    customer_id: int
    block_id: int
    product_id: int
    quantities_id: int
    regularity: int
    instance_id: Optional[str] = None
    net_price_single: Optional[str] = None
    minimum_minute: Optional[int] = None
    maximum_hour: Optional[int] = None
    maximum_task: Optional[int] = None
    admin_comment: Optional[str] = None
    pre_paid: Optional[int] = None
    is_repetitive: Optional[int] = None
    is_booking: Optional[int] = None
    active: Optional[int] = None


@dataclass
class ProjectCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id_: Optional[int] = None
    code: Optional[str] = None


@dataclass
class ProjectInactivateRequest:
    code: str
    instance_id: Optional[str] = None


@dataclass
class ProjectInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectTimesheetListRequest:
    code: str
    instance_id: Optional[str] = None


@dataclass
class ProjectTimesheetListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheets: Optional[list[dict[str, Any]]] = None


@dataclass
class ProjectTimesheetStartRequest:
    code: str
    projects_workers_id: int
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectTimesheetStartResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectTimesheetStopRequest:
    timesheet_id: int
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectTimesheetStopResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingSlotCreateRequest:
    code: str
    projects_workers_id: int
    start_date: str
    stop_date: str
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectBookingSlotCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    slot_id: Optional[int] = None


@dataclass
class ProjectBookingBookRequest:
    timesheet_id: int
    customer_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingBookResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCancelRequest:
    timesheet_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingCancelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCloseRequest:
    timesheet_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingBookDateRangeRequest:
    code: str
    customer_id: int
    date_from: str
    date_to: str
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingBookDateRangeResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None
    nights: Optional[int] = None


@dataclass
class ProjectBookingCancelGroupRequest:
    booking_group_id: str
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingCancelGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupRequest:
    booking_group_id: str
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingSetSlotPriceRequest:
    timesheet_id: int
    instance_id: Optional[str] = None
    net_price_override: Optional[str] = None


@dataclass
class ProjectBookingSetSlotPriceResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectAvailableSlotsRequest:
    code: str
    date_from: str
    date_to: str
    instance_id: Optional[str] = None


@dataclass
class ProjectAvailableSlotsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    slots: Optional[list[dict[str, Any]]] = None


@dataclass
class ProjectWorkerListRequest:
    instance_id: Optional[str] = None


@dataclass
class ProjectWorkerListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    workers: Optional[list[dict[str, Any]]] = None


@dataclass
class ProjectCalendarRequest:
    code: str
    year: int
    month: int
    instance_id: Optional[str] = None


@dataclass
class ProjectCalendarResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    calendar: Optional[str] = None


@dataclass
class ProjectPassCreateRequest:
    code: str
    customer_id: int
    total_occasions: int
    instance_id: Optional[str] = None
    product_id: Optional[int] = None
    net_price_single: Optional[str] = None
    auto_invoice: Optional[int] = None
    expiry_date: Optional[str] = None


@dataclass
class ProjectPassCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    pass_id: Optional[int] = None


@dataclass
class ProjectPassListRequest:
    code: str
    instance_id: Optional[str] = None


@dataclass
class ProjectPassListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    passes: Optional[list[dict[str, Any]]] = None


@dataclass
class ProjectPassDeactivateRequest:
    pass_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectPassDeactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class ProjectPassUpdateExpiryRequest:
    pass_id: int
    expiry_date: str
    instance_id: Optional[str] = None


@dataclass
class ProjectPassUpdateExpiryResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class TaxListRequest:
    instance_id: str
    type_: str


@dataclass
class TaxListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    value: Optional[float] = None
    active: Optional[int] = None
    is_default: Optional[int] = None
    vatType: Optional[str] = None
    vatSubType: Optional[str] = None
    taxTypeDesc: Optional[str] = None


@dataclass
class TaxAddRequest:
    instance_id: str
    name: str
    code: str
    value: float
    is_default: Optional[int] = None
    other: Optional[str] = None


@dataclass
class TaxAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxModifyRequest:
    instance_id: str
    name: str
    code: str
    value: float
    is_default: Optional[int] = None
    other: Optional[str] = None


@dataclass
class TaxModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxActivateRequest:
    instance_id: str
    code: str


@dataclass
class TaxActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxInactivateRequest:
    instance_id: str
    code: str


@dataclass
class TaxInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class PaymentModeInactivateRequest:
    instance_id: str
    code: str


@dataclass
class PaymentModeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeActivateRequest:
    instance_id: str
    code: str


@dataclass
class PaymentModeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeDownloadRequest:
    instance_id: str


@dataclass
class PaymentModeDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    active: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class OrderAddRequest:
    instance_id: str
    proform_order: int
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None
    meta: Optional[list[dict[str, Any]]] = None
    KULCS: Optional[str] = None


@dataclass
class OrderAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class OrderCollectiveAddRequest:
    instance_id: str
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None


@dataclass
class OrderCollectiveAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None


@dataclass
class OrderListRequest:
    instance_id: str
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    customer_sid: Optional[str] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    type_: Optional[str] = None


@dataclass
class OrderListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    orders: Optional[list[dict[str, Any]]] = None
    order_number: Optional[str] = None
    block_id: Optional[int] = None
    print_date: Optional[str] = None
    trade_date: Optional[str] = None
    pay_date: Optional[str] = None
    order_date: Optional[str] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    collective: Optional[int] = None
    type_: Optional[int] = None
    type_code: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode_code: Optional[str] = None
    comment: Optional[str] = None
    admin_comment: Optional[str] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency_id: Optional[int] = None
    currency: Optional[str] = None
    customer_sid: Optional[str] = None
    customer_legal_status: Optional[str] = None
    customer_name: Optional[str] = None
    customer_country: Optional[str] = None
    customer_city: Optional[str] = None
    customer_postcode: Optional[str] = None
    customer_street: Optional[str] = None
    customer_email: Optional[str] = None
    customer_tax_number: Optional[str] = None
    customer_eu_tax_number: Optional[str] = None
    customer_lang: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderStornoRequest:
    instance_id: str
    order_number: str
    admin_comment: Optional[str] = None
    storno_reason: Optional[str] = None
    refund: Optional[int] = None
    comment: Optional[str] = None


@dataclass
class OrderStornoResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class OrderProformDownloadRequest:
    instance_id: str
    order_number: str


@dataclass
class OrderProformDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    proform_id: Optional[int] = None
    proform_number: Optional[str] = None
    proform_file_size: Optional[int] = None
    proform: Optional[str] = None


@dataclass
class OrderBillRequest:
    instance_id: str
    order_number: str
    paid: int
    payment_mode_id: Optional[int] = None


@dataclass
class OrderBillResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None
    invoices: Optional[list[dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class OrderDetailsRequest:
    instance_id: str
    order_number: str


@dataclass
class OrderDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[int] = None
    net_price: Optional[str] = None
    tax_value: Optional[str] = None
    gross_price: Optional[str] = None
    elements: Optional[list[dict[str, Any]]] = None
    product_sid: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    collective: Optional[int] = None
    regularities_id: Optional[int] = None
    regularities_date: Optional[str] = None
    invoices: Optional[str] = None
    admin_comment: Optional[str] = None
    api_invoice: Optional[int] = None


@dataclass
class OrderCollectiveCloseRequest:
    instance_id: str
    customer_sid: str


@dataclass
class OrderCollectiveCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class OrderCollectiveSettlingRequest:
    instance_id: str
    order_number: str
    invoice_number: str


@dataclass
class OrderCollectiveSettlingResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    services_sid: Optional[str] = None
    service: Optional[str] = None
    amount: Optional[float] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency: Optional[str] = None
    confirmed: Optional[int] = None
    other: Optional[str] = None


@dataclass
class OrderCollectiveAddElementsRequest:
    instance_id: str
    customer_sid: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    comment: Optional[str] = None
    other: Optional[str] = None


@dataclass
class OrderCollectiveAddElementsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None


@dataclass
class OrderSetPaidRequest:
    instance_id: str
    order_number: str


@dataclass
class OrderSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderCheckPaidRequest:
    instance_id: str
    order_number: str


@dataclass
class OrderCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderPaidChangeListRequest:
    instance_id: str


@dataclass
class OrderPaidChangeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    order_number: Optional[str] = None


@dataclass
class InvoiceAddRequest:
    instance_id: str
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    prepayment: int
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceAddPrepaymentRequest:
    instance_id: str
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddPrepaymentResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceAddFinalRequest:
    instance_id: str
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: list[dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddFinalResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceDetailsRequest:
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[int] = None
    net_price: Optional[str] = None
    tax_value: Optional[str] = None
    gross_price: Optional[str] = None
    elements: Optional[list[dict[str, Any]]] = None
    product_sid: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    tax_code: Optional[str] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    block_name: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    api_invoice: Optional[int] = None


@dataclass
class InvoiceDownloadRequest:
    instance_id: str
    invoice_number: str
    invoice_type: str


@dataclass
class InvoiceDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoices: Optional[list[dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_number: Optional[str] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class InvoiceStornoRequest:
    instance_id: str
    invoice_number: str
    admin_comment: Optional[str] = None
    storno_reason: Optional[str] = None
    refund: Optional[int] = None
    comment: Optional[str] = None


@dataclass
class InvoiceStornoResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class InvoiceListRequest:
    instance_id: str
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    customer_sid: Optional[str] = None


@dataclass
class InvoiceListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    invoices: Optional[list[dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    customer_legal_status: Optional[str] = None
    customer_name: Optional[str] = None
    customer_country: Optional[str] = None
    customer_postcode: Optional[str] = None
    customer_city: Optional[str] = None
    customer_street: Optional[str] = None
    customer_street_number: Optional[str] = None
    customer_door: Optional[str] = None
    customer_tax_number: Optional[str] = None
    customer_eu_tax_number: Optional[str] = None
    customer_region: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_email: Optional[str] = None
    customer_lang: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    type_: Optional[int] = None
    type_code: Optional[str] = None
    reference: Optional[str] = None
    payment_mode_id: Optional[int] = None
    comment: Optional[int] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class InvoiceExportRequest:
    instance_id: str
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    number_from: Optional[str] = None
    number_to: Optional[str] = None


@dataclass
class InvoiceExportResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_export_file: Optional[str] = None


@dataclass
class InvoiceSearchRequest:
    instance_id: str
    search_type_code: str
    search: str


@dataclass
class InvoiceSearchResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency_id: Optional[int] = None
    currency: Optional[str] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode_code: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[str] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    elements: Optional[list[dict[str, Any]]] = None
    product_sid: Optional[str] = None
    product_name: Optional[str] = None
    product_service_id: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    invoice_type: Optional[str] = None


@dataclass
class InvoiceCorrectionRequest:
    instance_id: str
    invoice_number: str
    elementsStorno: list[dict[str, Any]]
    elements: list[dict[str, Any]]
    quantity: str
    net_price_single: float
    tax_code: str
    payment_mode_id: int
    product_sid: Optional[int] = None
    amount: Optional[int] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    trade_date: Optional[str] = None
    pay_date: Optional[str] = None
    paid: Optional[int] = None


@dataclass
class InvoiceCorrectionResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class InvoiceResendRequest:
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceResendResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None


@dataclass
class InvoiceCheckPaidRequest:
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class InvoiceSetPaidRequest:
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class DebtDetailsRequest:
    instance_id: str
    type_: str
    customer_sid: str
    invoice_number: str


@dataclass
class DebtDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt: Optional[Any] = None


@dataclass
class DebtDownloadRequest:
    instance_id: str
    invoice_number: str
    invoice_type: str


@dataclass
class DebtDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[int] = None


@dataclass
class DebtListRequest:
    instance_id: str
    type_: Optional[int] = None
    active: Optional[int] = None
    paid: Optional[int] = None
    customer_sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None


@dataclass
class DebtListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    list_: Optional[list[dict[str, Any]]] = None


@dataclass
class DebtAddRequest:
    instance_id: str
    customer_sid: str
    invoice_number: str
    amount: float
    currency: str
    trade_date: str
    print_date: str
    pay_date: str
    currency_id: Optional[int] = None
    payment_date: Optional[str] = None
    payment_mode: Optional[str] = None
    payment_mode_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    cost_centre: Optional[str] = None
    cost_type: Optional[str] = None
    invoice_reference: Optional[str] = None
    bank_comment: Optional[str] = None
    comment: Optional[str] = None
    invoice_file: Optional[str] = None


@dataclass
class DebtAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt_id: Optional[int] = None


@dataclass
class DebtModifyRequest:
    instance_id: str
    id_: int
    customer_sid: Optional[str] = None
    invoice_number: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    payment_date: Optional[str] = None
    payment_mode: Optional[str] = None
    payment_mode_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    cost_centre: Optional[str] = None
    cost_type: Optional[str] = None
    invoice_reference: Optional[str] = None
    bank_comment: Optional[str] = None
    comment: Optional[str] = None
    invoice_file: Optional[str] = None


@dataclass
class DebtModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt_id: Optional[int] = None


@dataclass
class DebtAcceptRequest:
    instance_id: str
    debt_ids: list[dict[str, Any]]


@dataclass
class DebtAcceptResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    accepted_count: Optional[int] = None


@dataclass
class DebtPayRequest:
    instance_id: str
    debt_ids: list[dict[str, Any]]


@dataclass
class DebtPayResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid_count: Optional[int] = None


@dataclass
class DebtDeleteRequest:
    instance_id: str
    debt_ids: list[dict[str, Any]]


@dataclass
class DebtDeleteResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    deleted_count: Optional[int] = None


@dataclass
class DebtGenerateRequest:
    instance_id: str
    debt_ids: list[dict[str, Any]]


@dataclass
class DebtGenerateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[int] = None


@dataclass
class DebtExportRequest:
    instance_id: str
    dateFrom: str
    dateTo: str


@dataclass
class DebtExportResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None


@dataclass
class SystemMessageListRequest:
    instance_id: str


@dataclass
class SystemMessageListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    message: Optional[str] = None
    message_date: Optional[str] = None
    message_type: Optional[int] = None


@dataclass
class SystemMessageSetReadRequest:
    instance_id: str
    id_: int


@dataclass
class SystemMessageSetReadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class SystemErrorCodeListRequest:
    instance_id: str
    lang: Optional[str] = None


@dataclass
class SystemErrorCodeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    lang: Optional[list[dict[str, Any]]] = None
    code: Optional[int] = None
    description: Optional[str] = None
    type_: Optional[str] = None


@dataclass
class GetVersionRequest:
    instance_id: str


@dataclass
class GetVersionResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    version: Optional[str] = None


@dataclass
class ServiceProviderDatasRequest:
    instance_id: str


@dataclass
class ServiceProviderDatasResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    hosting_name: Optional[str] = None
    hosting_address: Optional[str] = None
    hosting_tax_number: Optional[str] = None
    hosting_email: Optional[str] = None
    hosting_phone: Optional[str] = None
    hosting_customer_service_langs: Optional[str] = None
    hosting_customer_service_times: Optional[str] = None
    hosting_bank_name: Optional[str] = None
    hosting_bank_number: Optional[str] = None
    hosting_service_url: Optional[str] = None
    hosting_service_start_date: Optional[str] = None
    hosting_service_version: Optional[str] = None
    instance_web_url: Optional[str] = None
    instance_soap_url: Optional[str] = None
    instance_rest_url: Optional[str] = None


@dataclass
class CompanyDataRequest:
    instance_id: str


@dataclass
class CompanyDataResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id_: Optional[int] = None
    block_name: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    bank_number: Optional[str] = None
    invoice_number_pre: Optional[str] = None
    invoice_number_length: Optional[int] = None
    email: Optional[str] = None
    comment: Optional[str] = None
    invoice_footer: Optional[str] = None
    invoice_issue: Optional[int] = None
    restart_number_by_year: Optional[int] = None
    lang: Optional[str] = None
    date: Optional[str] = None
    invoice_template: Optional[str] = None
    admin_users_id: Optional[int] = None
    currency_id: Optional[int] = None
    active: Optional[int] = None
    bank_name: Optional[str] = None
    currency: Optional[str] = None


@dataclass
class QuantityListRequest:
    instance_id: str
    type_: str


@dataclass
class QuantityListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    active: Optional[int] = None
    is_default: Optional[int] = None
    unitOfMeasure: Optional[str] = None


@dataclass
class CurrencyDownloadRequest:
    instance_id: str
    type_: str


@dataclass
class CurrencyDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[float] = None
    date: Optional[str] = None


@dataclass
class RegularityDownloadRequest:
    instance_id: str


@dataclass
class RegularityDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    id_: Optional[int] = None
    code: Optional[str] = None
    regularity: Optional[str] = None


@dataclass
class CountryDownloadRequest:
    instance_id: str


@dataclass
class CountryDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    code: Optional[str] = None
    country: Optional[str] = None


@dataclass
class PostcodeDownloadRequest:
    instance_id: str
    country: str


@dataclass
class PostcodeDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    postcodes: Optional[list[dict[str, Any]]] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None


@dataclass
class PingRequest:
    instance_id: str


@dataclass
class PingResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class MonitorRequest:
    instance_id: str


@dataclass
class MonitorResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list_: Optional[list[dict[str, Any]]] = None
    state: Optional[str] = None
    name: Optional[str] = None
    last_check: Optional[str] = None


class SzamlaiktatoAPI:
    def __init__(self, client: OnlineSzamlazoClient):
        self.client = client

    def install(
        self, request: InstallRequest, skip_block: bool = False
    ) -> InstallResponse:
        params = asdict(request) if request else {}
        data = self.client._call("install", params, skip_block=skip_block)
        valid_keys = InstallResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InstallResponse(**filtered_data)

    def update(
        self, request: UpdateRequest, skip_block: bool = False
    ) -> UpdateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("update", params, skip_block=skip_block)
        valid_keys = UpdateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return UpdateResponse(**filtered_data)

    def customerAdd(
        self, request: CustomerAddRequest, skip_block: bool = False
    ) -> CustomerAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerAdd", params, skip_block=skip_block)
        valid_keys = CustomerAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerAddResponse(**filtered_data)

    def customerModify(
        self, request: CustomerModifyRequest, skip_block: bool = False
    ) -> CustomerModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerModify", params, skip_block=skip_block)
        valid_keys = CustomerModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerModifyResponse(**filtered_data)

    def customerGet(
        self, request: CustomerGetRequest, skip_block: bool = False
    ) -> CustomerGetResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerGet", params, skip_block=skip_block)
        valid_keys = CustomerGetResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerGetResponse(**filtered_data)

    def customerActivate(
        self, request: CustomerActivateRequest, skip_block: bool = False
    ) -> CustomerActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerActivate", params, skip_block=skip_block)
        valid_keys = CustomerActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerActivateResponse(**filtered_data)

    def customerInactivate(
        self, request: CustomerInactivateRequest, skip_block: bool = False
    ) -> CustomerInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerInactivate", params, skip_block=skip_block)
        valid_keys = CustomerInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerInactivateResponse(**filtered_data)

    def customerSwap(
        self, request: CustomerSwapRequest, skip_block: bool = False
    ) -> CustomerSwapResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerSwap", params, skip_block=skip_block)
        valid_keys = CustomerSwapResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerSwapResponse(**filtered_data)

    def customerList(
        self, request: CustomerListRequest, skip_block: bool = False
    ) -> CustomerListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("customerList", params, skip_block=skip_block)
        valid_keys = CustomerListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CustomerListResponse(**filtered_data)

    def productAdd(
        self, request: ProductAddRequest, skip_block: bool = False
    ) -> ProductAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productAdd", params, skip_block=skip_block)
        valid_keys = ProductAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductAddResponse(**filtered_data)

    def productModify(
        self, request: ProductModifyRequest, skip_block: bool = False
    ) -> ProductModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productModify", params, skip_block=skip_block)
        valid_keys = ProductModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductModifyResponse(**filtered_data)

    def productGet(
        self, request: ProductGetRequest, skip_block: bool = False
    ) -> ProductGetResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productGet", params, skip_block=skip_block)
        valid_keys = ProductGetResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductGetResponse(**filtered_data)

    def productActivate(
        self, request: ProductActivateRequest, skip_block: bool = False
    ) -> ProductActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productActivate", params, skip_block=skip_block)
        valid_keys = ProductActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductActivateResponse(**filtered_data)

    def productInactivate(
        self, request: ProductInactivateRequest, skip_block: bool = False
    ) -> ProductInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productInactivate", params, skip_block=skip_block)
        valid_keys = ProductInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductInactivateResponse(**filtered_data)

    def productList(
        self, request: ProductListRequest, skip_block: bool = False
    ) -> ProductListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = ProductListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductListResponse(**filtered_data)

    def productFileList(
        self, request: ProductFileListRequest, skip_block: bool = False
    ) -> ProductFileListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("productFileList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = ProductFileListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProductFileListResponse(**filtered_data)

    def outerDatasources(
        self, request: OuterDatasourcesRequest, skip_block: bool = False
    ) -> OuterDatasourcesResponse:
        params = asdict(request) if request else {}
        data = self.client._call("outerDatasources", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = OuterDatasourcesResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OuterDatasourcesResponse(**filtered_data)

    def outerDatasourcesGet(
        self, request: OuterDatasourcesGetRequest, skip_block: bool = False
    ) -> OuterDatasourcesGetResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("outerDatasourcesGet", params, skip_block=skip_block)
        valid_keys = OuterDatasourcesGetResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OuterDatasourcesGetResponse(**filtered_data)

    def outerDatasourcesSave(
        self, request: OuterDatasourcesSaveRequest, skip_block: bool = False
    ) -> OuterDatasourcesSaveResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("outerDatasourcesSave", params, skip_block=skip_block)
        valid_keys = OuterDatasourcesSaveResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OuterDatasourcesSaveResponse(**filtered_data)

    def adminUserAdd(
        self, request: AdminUserAddRequest, skip_block: bool = False
    ) -> AdminUserAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("adminUserAdd", params, skip_block=skip_block)
        valid_keys = AdminUserAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return AdminUserAddResponse(**filtered_data)

    def adminUserPassword(
        self, request: AdminUserPasswordRequest, skip_block: bool = False
    ) -> AdminUserPasswordResponse:
        params = asdict(request) if request else {}
        data = self.client._call("adminUserPassword", params, skip_block=skip_block)
        valid_keys = AdminUserPasswordResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return AdminUserPasswordResponse(**filtered_data)

    def adminUserDel(
        self, request: AdminUserDelRequest, skip_block: bool = False
    ) -> AdminUserDelResponse:
        params = asdict(request) if request else {}
        data = self.client._call("adminUserDel", params, skip_block=skip_block)
        valid_keys = AdminUserDelResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return AdminUserDelResponse(**filtered_data)

    def blockAdd(
        self, request: BlockAddRequest, skip_block: bool = False
    ) -> BlockAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("blockAdd", params, skip_block=skip_block)
        valid_keys = BlockAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockAddResponse(**filtered_data)

    def blockUpdateCompanyData(
        self, request: BlockUpdateCompanyDataRequest, skip_block: bool = False
    ) -> BlockUpdateCompanyDataResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "blockUpdateCompanyData", params, skip_block=skip_block
        )
        valid_keys = BlockUpdateCompanyDataResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockUpdateCompanyDataResponse(**filtered_data)

    def blockModify(
        self, request: BlockModifyRequest, skip_block: bool = False
    ) -> BlockModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("blockModify", params, skip_block=skip_block)
        valid_keys = BlockModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockModifyResponse(**filtered_data)

    def blockList(
        self, request: BlockListRequest, skip_block: bool = False
    ) -> BlockListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("blockList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = BlockListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockListResponse(**filtered_data)

    def blockClose(
        self, request: BlockCloseRequest, skip_block: bool = False
    ) -> BlockCloseResponse:
        params = asdict(request) if request else {}
        data = self.client._call("blockClose", params, skip_block=skip_block)
        valid_keys = BlockCloseResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockCloseResponse(**filtered_data)

    def blockOpen(
        self, request: BlockOpenRequest, skip_block: bool = False
    ) -> BlockOpenResponse:
        params = asdict(request) if request else {}
        data = self.client._call("blockOpen", params, skip_block=skip_block)
        valid_keys = BlockOpenResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return BlockOpenResponse(**filtered_data)

    def costCentreAdd(
        self, request: CostCentreAddRequest, skip_block: bool = False
    ) -> CostCentreAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costCentreAdd", params, skip_block=skip_block)
        valid_keys = CostCentreAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostCentreAddResponse(**filtered_data)

    def costCentreModify(
        self, request: CostCentreModifyRequest, skip_block: bool = False
    ) -> CostCentreModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costCentreModify", params, skip_block=skip_block)
        valid_keys = CostCentreModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostCentreModifyResponse(**filtered_data)

    def costCentreList(
        self, request: CostCentreListRequest, skip_block: bool = False
    ) -> CostCentreListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costCentreList", params, skip_block=skip_block)
        valid_keys = CostCentreListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostCentreListResponse(**filtered_data)

    def costCentreActivate(
        self, request: CostCentreActivateRequest, skip_block: bool = False
    ) -> CostCentreActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costCentreActivate", params, skip_block=skip_block)
        valid_keys = CostCentreActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostCentreActivateResponse(**filtered_data)

    def costCentreInactivate(
        self, request: CostCentreInactivateRequest, skip_block: bool = False
    ) -> CostCentreInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costCentreInactivate", params, skip_block=skip_block)
        valid_keys = CostCentreInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostCentreInactivateResponse(**filtered_data)

    def costTypeAdd(
        self, request: CostTypeAddRequest, skip_block: bool = False
    ) -> CostTypeAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costTypeAdd", params, skip_block=skip_block)
        valid_keys = CostTypeAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostTypeAddResponse(**filtered_data)

    def costTypeModify(
        self, request: CostTypeModifyRequest, skip_block: bool = False
    ) -> CostTypeModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costTypeModify", params, skip_block=skip_block)
        valid_keys = CostTypeModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostTypeModifyResponse(**filtered_data)

    def costTypeList(
        self, request: CostTypeListRequest, skip_block: bool = False
    ) -> CostTypeListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costTypeList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = CostTypeListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostTypeListResponse(**filtered_data)

    def costTypeActivate(
        self, request: CostTypeActivateRequest, skip_block: bool = False
    ) -> CostTypeActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costTypeActivate", params, skip_block=skip_block)
        valid_keys = CostTypeActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostTypeActivateResponse(**filtered_data)

    def costTypeInactivate(
        self, request: CostTypeInactivateRequest, skip_block: bool = False
    ) -> CostTypeInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("costTypeInactivate", params, skip_block=skip_block)
        valid_keys = CostTypeInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CostTypeInactivateResponse(**filtered_data)

    def projectList(
        self, request: ProjectListRequest, skip_block: bool = False
    ) -> ProjectListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectList", params, skip_block=skip_block)
        valid_keys = ProjectListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectListResponse(**filtered_data)

    def projectGet(
        self, request: ProjectGetRequest, skip_block: bool = False
    ) -> ProjectGetResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectGet", params, skip_block=skip_block)
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = ProjectGetResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectGetResponse(**filtered_data)

    def projectCreate(
        self, request: ProjectCreateRequest, skip_block: bool = False
    ) -> ProjectCreateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectCreate", params, skip_block=skip_block)
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = ProjectCreateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectCreateResponse(**filtered_data)

    def projectInactivate(
        self, request: ProjectInactivateRequest, skip_block: bool = False
    ) -> ProjectInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectInactivate", params, skip_block=skip_block)
        valid_keys = ProjectInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectInactivateResponse(**filtered_data)

    def projectTimesheetList(
        self, request: ProjectTimesheetListRequest, skip_block: bool = False
    ) -> ProjectTimesheetListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectTimesheetList", params, skip_block=skip_block)
        valid_keys = ProjectTimesheetListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectTimesheetListResponse(**filtered_data)

    def projectTimesheetStart(
        self, request: ProjectTimesheetStartRequest, skip_block: bool = False
    ) -> ProjectTimesheetStartResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectTimesheetStart", params, skip_block=skip_block)
        valid_keys = ProjectTimesheetStartResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectTimesheetStartResponse(**filtered_data)

    def projectTimesheetStop(
        self, request: ProjectTimesheetStopRequest, skip_block: bool = False
    ) -> ProjectTimesheetStopResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectTimesheetStop", params, skip_block=skip_block)
        valid_keys = ProjectTimesheetStopResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectTimesheetStopResponse(**filtered_data)

    def projectBookingSlotCreate(
        self, request: ProjectBookingSlotCreateRequest, skip_block: bool = False
    ) -> ProjectBookingSlotCreateResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectBookingSlotCreate", params, skip_block=skip_block
        )
        valid_keys = ProjectBookingSlotCreateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingSlotCreateResponse(**filtered_data)

    def projectBookingBook(
        self, request: ProjectBookingBookRequest, skip_block: bool = False
    ) -> ProjectBookingBookResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectBookingBook", params, skip_block=skip_block)
        valid_keys = ProjectBookingBookResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingBookResponse(**filtered_data)

    def projectBookingCancel(
        self, request: ProjectBookingCancelRequest, skip_block: bool = False
    ) -> ProjectBookingCancelResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectBookingCancel", params, skip_block=skip_block)
        valid_keys = ProjectBookingCancelResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingCancelResponse(**filtered_data)

    def projectBookingClose(
        self, request: ProjectBookingCloseRequest, skip_block: bool = False
    ) -> ProjectBookingCloseResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectBookingClose", params, skip_block=skip_block)
        valid_keys = ProjectBookingCloseResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingCloseResponse(**filtered_data)

    def projectBookingBookDateRange(
        self, request: ProjectBookingBookDateRangeRequest, skip_block: bool = False
    ) -> ProjectBookingBookDateRangeResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectBookingBookDateRange", params, skip_block=skip_block
        )
        valid_keys = ProjectBookingBookDateRangeResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingBookDateRangeResponse(**filtered_data)

    def projectBookingCancelGroup(
        self, request: ProjectBookingCancelGroupRequest, skip_block: bool = False
    ) -> ProjectBookingCancelGroupResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectBookingCancelGroup", params, skip_block=skip_block
        )
        valid_keys = ProjectBookingCancelGroupResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingCancelGroupResponse(**filtered_data)

    def projectBookingCloseGroup(
        self, request: ProjectBookingCloseGroupRequest, skip_block: bool = False
    ) -> ProjectBookingCloseGroupResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectBookingCloseGroup", params, skip_block=skip_block
        )
        valid_keys = ProjectBookingCloseGroupResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingCloseGroupResponse(**filtered_data)

    def projectBookingSetSlotPrice(
        self, request: ProjectBookingSetSlotPriceRequest, skip_block: bool = False
    ) -> ProjectBookingSetSlotPriceResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectBookingSetSlotPrice", params, skip_block=skip_block
        )
        valid_keys = ProjectBookingSetSlotPriceResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectBookingSetSlotPriceResponse(**filtered_data)

    def projectAvailableSlots(
        self, request: ProjectAvailableSlotsRequest, skip_block: bool = False
    ) -> ProjectAvailableSlotsResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectAvailableSlots", params, skip_block=skip_block)
        valid_keys = ProjectAvailableSlotsResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectAvailableSlotsResponse(**filtered_data)

    def projectWorkerList(
        self, request: ProjectWorkerListRequest, skip_block: bool = False
    ) -> ProjectWorkerListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectWorkerList", params, skip_block=skip_block)
        valid_keys = ProjectWorkerListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectWorkerListResponse(**filtered_data)

    def projectCalendar(
        self, request: ProjectCalendarRequest, skip_block: bool = False
    ) -> ProjectCalendarResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectCalendar", params, skip_block=skip_block)
        valid_keys = ProjectCalendarResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectCalendarResponse(**filtered_data)

    def projectPassCreate(
        self, request: ProjectPassCreateRequest, skip_block: bool = False
    ) -> ProjectPassCreateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectPassCreate", params, skip_block=skip_block)
        valid_keys = ProjectPassCreateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectPassCreateResponse(**filtered_data)

    def projectPassList(
        self, request: ProjectPassListRequest, skip_block: bool = False
    ) -> ProjectPassListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectPassList", params, skip_block=skip_block)
        valid_keys = ProjectPassListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectPassListResponse(**filtered_data)

    def projectPassDeactivate(
        self, request: ProjectPassDeactivateRequest, skip_block: bool = False
    ) -> ProjectPassDeactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("projectPassDeactivate", params, skip_block=skip_block)
        valid_keys = ProjectPassDeactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectPassDeactivateResponse(**filtered_data)

    def projectPassUpdateExpiry(
        self, request: ProjectPassUpdateExpiryRequest, skip_block: bool = False
    ) -> ProjectPassUpdateExpiryResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "projectPassUpdateExpiry", params, skip_block=skip_block
        )
        valid_keys = ProjectPassUpdateExpiryResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ProjectPassUpdateExpiryResponse(**filtered_data)

    def taxList(
        self, request: TaxListRequest, skip_block: bool = False
    ) -> TaxListResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("taxList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = TaxListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return TaxListResponse(**filtered_data)

    def taxAdd(
        self, request: TaxAddRequest, skip_block: bool = False
    ) -> TaxAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("taxAdd", params, skip_block=skip_block)
        valid_keys = TaxAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return TaxAddResponse(**filtered_data)

    def taxModify(
        self, request: TaxModifyRequest, skip_block: bool = False
    ) -> TaxModifyResponse:
        params = asdict(request) if request else {}
        data = self.client._call("taxModify", params, skip_block=skip_block)
        valid_keys = TaxModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return TaxModifyResponse(**filtered_data)

    def taxActivate(
        self, request: TaxActivateRequest, skip_block: bool = False
    ) -> TaxActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("taxActivate", params, skip_block=skip_block)
        valid_keys = TaxActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return TaxActivateResponse(**filtered_data)

    def taxInactivate(
        self, request: TaxInactivateRequest, skip_block: bool = False
    ) -> TaxInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("taxInactivate", params, skip_block=skip_block)
        valid_keys = TaxInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return TaxInactivateResponse(**filtered_data)

    def paymentModeInactivate(
        self, request: PaymentModeInactivateRequest, skip_block: bool = False
    ) -> PaymentModeInactivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("paymentModeInactivate", params, skip_block=skip_block)
        valid_keys = PaymentModeInactivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return PaymentModeInactivateResponse(**filtered_data)

    def paymentModeActivate(
        self, request: PaymentModeActivateRequest, skip_block: bool = False
    ) -> PaymentModeActivateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("paymentModeActivate", params, skip_block=skip_block)
        valid_keys = PaymentModeActivateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return PaymentModeActivateResponse(**filtered_data)

    def paymentModeDownload(
        self, request: PaymentModeDownloadRequest, skip_block: bool = False
    ) -> PaymentModeDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("paymentModeDownload", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = PaymentModeDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return PaymentModeDownloadResponse(**filtered_data)

    def orderAdd(
        self, request: OrderAddRequest, skip_block: bool = False
    ) -> OrderAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderAdd", params, skip_block=skip_block)
        valid_keys = OrderAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderAddResponse(**filtered_data)

    def orderCollectiveAdd(
        self, request: OrderCollectiveAddRequest, skip_block: bool = False
    ) -> OrderCollectiveAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderCollectiveAdd", params, skip_block=skip_block)
        valid_keys = OrderCollectiveAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderCollectiveAddResponse(**filtered_data)

    def orderList(
        self, request: OrderListRequest, skip_block: bool = False
    ) -> OrderListResponse:
        params = asdict(request) if request else {}
        if "from_" in params:
            params["from"] = params.pop("from_")
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("orderList", params, skip_block=skip_block)
        if "type" in data:
            data["type_"] = data.pop("type")
        valid_keys = OrderListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderListResponse(**filtered_data)

    def orderStorno(
        self, request: OrderStornoRequest, skip_block: bool = False
    ) -> OrderStornoResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderStorno", params, skip_block=skip_block)
        valid_keys = OrderStornoResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderStornoResponse(**filtered_data)

    def orderProformDownload(
        self, request: OrderProformDownloadRequest, skip_block: bool = False
    ) -> OrderProformDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderProformDownload", params, skip_block=skip_block)
        valid_keys = OrderProformDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderProformDownloadResponse(**filtered_data)

    def orderBill(
        self, request: OrderBillRequest, skip_block: bool = False
    ) -> OrderBillResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderBill", params, skip_block=skip_block)
        valid_keys = OrderBillResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderBillResponse(**filtered_data)

    def orderDetails(
        self, request: OrderDetailsRequest, skip_block: bool = False
    ) -> OrderDetailsResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderDetails", params, skip_block=skip_block)
        valid_keys = OrderDetailsResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderDetailsResponse(**filtered_data)

    def orderCollectiveClose(
        self, request: OrderCollectiveCloseRequest, skip_block: bool = False
    ) -> OrderCollectiveCloseResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderCollectiveClose", params, skip_block=skip_block)
        valid_keys = OrderCollectiveCloseResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderCollectiveCloseResponse(**filtered_data)

    def orderCollectiveSettling(
        self, request: OrderCollectiveSettlingRequest, skip_block: bool = False
    ) -> OrderCollectiveSettlingResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "orderCollectiveSettling", params, skip_block=skip_block
        )
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = OrderCollectiveSettlingResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderCollectiveSettlingResponse(**filtered_data)

    def orderCollectiveAddElements(
        self, request: OrderCollectiveAddElementsRequest, skip_block: bool = False
    ) -> OrderCollectiveAddElementsResponse:
        params = asdict(request) if request else {}
        data = self.client._call(
            "orderCollectiveAddElements", params, skip_block=skip_block
        )
        valid_keys = OrderCollectiveAddElementsResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderCollectiveAddElementsResponse(**filtered_data)

    def orderSetPaid(
        self, request: OrderSetPaidRequest, skip_block: bool = False
    ) -> OrderSetPaidResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderSetPaid", params, skip_block=skip_block)
        valid_keys = OrderSetPaidResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderSetPaidResponse(**filtered_data)

    def orderCheckPaid(
        self, request: OrderCheckPaidRequest, skip_block: bool = False
    ) -> OrderCheckPaidResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderCheckPaid", params, skip_block=skip_block)
        valid_keys = OrderCheckPaidResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderCheckPaidResponse(**filtered_data)

    def orderPaidChangeList(
        self, request: OrderPaidChangeListRequest, skip_block: bool = False
    ) -> OrderPaidChangeListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("orderPaidChangeList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = OrderPaidChangeListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return OrderPaidChangeListResponse(**filtered_data)

    def invoiceAdd(
        self, request: InvoiceAddRequest, skip_block: bool = False
    ) -> InvoiceAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceAdd", params, skip_block=skip_block)
        valid_keys = InvoiceAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceAddResponse(**filtered_data)

    def invoiceAddPrepayment(
        self, request: InvoiceAddPrepaymentRequest, skip_block: bool = False
    ) -> InvoiceAddPrepaymentResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceAddPrepayment", params, skip_block=skip_block)
        valid_keys = InvoiceAddPrepaymentResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceAddPrepaymentResponse(**filtered_data)

    def invoiceAddFinal(
        self, request: InvoiceAddFinalRequest, skip_block: bool = False
    ) -> InvoiceAddFinalResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceAddFinal", params, skip_block=skip_block)
        valid_keys = InvoiceAddFinalResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceAddFinalResponse(**filtered_data)

    def invoiceDetails(
        self, request: InvoiceDetailsRequest, skip_block: bool = False
    ) -> InvoiceDetailsResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceDetails", params, skip_block=skip_block)
        valid_keys = InvoiceDetailsResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceDetailsResponse(**filtered_data)

    def invoiceDownload(
        self, request: InvoiceDownloadRequest, skip_block: bool = False
    ) -> InvoiceDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceDownload", params, skip_block=skip_block)
        valid_keys = InvoiceDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceDownloadResponse(**filtered_data)

    def invoiceStorno(
        self, request: InvoiceStornoRequest, skip_block: bool = False
    ) -> InvoiceStornoResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceStorno", params, skip_block=skip_block)
        valid_keys = InvoiceStornoResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceStornoResponse(**filtered_data)

    def invoiceList(
        self, request: InvoiceListRequest, skip_block: bool = False
    ) -> InvoiceListResponse:
        params = asdict(request) if request else {}
        if "from_" in params:
            params["from"] = params.pop("from_")
        data = self.client._call("invoiceList", params, skip_block=skip_block)
        if "type" in data:
            data["type_"] = data.pop("type")
        valid_keys = InvoiceListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceListResponse(**filtered_data)

    def invoiceExport(
        self, request: InvoiceExportRequest, skip_block: bool = False
    ) -> InvoiceExportResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceExport", params, skip_block=skip_block)
        valid_keys = InvoiceExportResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceExportResponse(**filtered_data)

    def invoiceSearch(
        self, request: InvoiceSearchRequest, skip_block: bool = False
    ) -> InvoiceSearchResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceSearch", params, skip_block=skip_block)
        valid_keys = InvoiceSearchResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceSearchResponse(**filtered_data)

    def invoiceCorrection(
        self, request: InvoiceCorrectionRequest, skip_block: bool = False
    ) -> InvoiceCorrectionResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceCorrection", params, skip_block=skip_block)
        valid_keys = InvoiceCorrectionResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceCorrectionResponse(**filtered_data)

    def invoiceResend(
        self, request: InvoiceResendRequest, skip_block: bool = False
    ) -> InvoiceResendResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceResend", params, skip_block=skip_block)
        valid_keys = InvoiceResendResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceResendResponse(**filtered_data)

    def invoiceCheckPaid(
        self, request: InvoiceCheckPaidRequest, skip_block: bool = False
    ) -> InvoiceCheckPaidResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceCheckPaid", params, skip_block=skip_block)
        valid_keys = InvoiceCheckPaidResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceCheckPaidResponse(**filtered_data)

    def invoiceSetPaid(
        self, request: InvoiceSetPaidRequest, skip_block: bool = False
    ) -> InvoiceSetPaidResponse:
        params = asdict(request) if request else {}
        data = self.client._call("invoiceSetPaid", params, skip_block=skip_block)
        valid_keys = InvoiceSetPaidResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return InvoiceSetPaidResponse(**filtered_data)

    def debtDetails(
        self, request: DebtDetailsRequest, skip_block: bool = False
    ) -> DebtDetailsResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("debtDetails", params, skip_block=skip_block)
        valid_keys = DebtDetailsResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtDetailsResponse(**filtered_data)

    def debtDownload(
        self, request: DebtDownloadRequest, skip_block: bool = False
    ) -> DebtDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtDownload", params, skip_block=skip_block)
        valid_keys = DebtDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtDownloadResponse(**filtered_data)

    def debtList(
        self, request: DebtListRequest, skip_block: bool = False
    ) -> DebtListResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        if "from_" in params:
            params["from"] = params.pop("from_")
        data = self.client._call("debtList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = DebtListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtListResponse(**filtered_data)

    def debtAdd(
        self, request: DebtAddRequest, skip_block: bool = False
    ) -> DebtAddResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtAdd", params, skip_block=skip_block)
        valid_keys = DebtAddResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtAddResponse(**filtered_data)

    def debtModify(
        self, request: DebtModifyRequest, skip_block: bool = False
    ) -> DebtModifyResponse:
        params = asdict(request) if request else {}
        if "id_" in params:
            params["id"] = params.pop("id_")
        data = self.client._call("debtModify", params, skip_block=skip_block)
        valid_keys = DebtModifyResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtModifyResponse(**filtered_data)

    def debtAccept(
        self, request: DebtAcceptRequest, skip_block: bool = False
    ) -> DebtAcceptResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtAccept", params, skip_block=skip_block)
        valid_keys = DebtAcceptResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtAcceptResponse(**filtered_data)

    def debtPay(
        self, request: DebtPayRequest, skip_block: bool = False
    ) -> DebtPayResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtPay", params, skip_block=skip_block)
        valid_keys = DebtPayResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtPayResponse(**filtered_data)

    def debtDelete(
        self, request: DebtDeleteRequest, skip_block: bool = False
    ) -> DebtDeleteResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtDelete", params, skip_block=skip_block)
        valid_keys = DebtDeleteResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtDeleteResponse(**filtered_data)

    def debtGenerate(
        self, request: DebtGenerateRequest, skip_block: bool = False
    ) -> DebtGenerateResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtGenerate", params, skip_block=skip_block)
        valid_keys = DebtGenerateResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtGenerateResponse(**filtered_data)

    def debtExport(
        self, request: DebtExportRequest, skip_block: bool = False
    ) -> DebtExportResponse:
        params = asdict(request) if request else {}
        data = self.client._call("debtExport", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = DebtExportResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return DebtExportResponse(**filtered_data)

    def systemMessageList(
        self, request: SystemMessageListRequest, skip_block: bool = False
    ) -> SystemMessageListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("systemMessageList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = SystemMessageListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return SystemMessageListResponse(**filtered_data)

    def systemMessageSetRead(
        self, request: SystemMessageSetReadRequest, skip_block: bool = False
    ) -> SystemMessageSetReadResponse:
        params = asdict(request) if request else {}
        if "id_" in params:
            params["id"] = params.pop("id_")
        data = self.client._call("systemMessageSetRead", params, skip_block=skip_block)
        valid_keys = SystemMessageSetReadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return SystemMessageSetReadResponse(**filtered_data)

    def systemErrorCodeList(
        self, request: SystemErrorCodeListRequest, skip_block: bool = False
    ) -> SystemErrorCodeListResponse:
        params = asdict(request) if request else {}
        data = self.client._call("systemErrorCodeList", params, skip_block=skip_block)
        if "type" in data:
            data["type_"] = data.pop("type")
        valid_keys = SystemErrorCodeListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return SystemErrorCodeListResponse(**filtered_data)

    def getVersion(
        self, request: GetVersionRequest, skip_block: bool = False
    ) -> GetVersionResponse:
        params = asdict(request) if request else {}
        data = self.client._call("getVersion", params, skip_block=skip_block)
        valid_keys = GetVersionResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return GetVersionResponse(**filtered_data)

    def serviceProviderDatas(
        self, request: ServiceProviderDatasRequest, skip_block: bool = False
    ) -> ServiceProviderDatasResponse:
        params = asdict(request) if request else {}
        data = self.client._call("serviceProviderDatas", params, skip_block=skip_block)
        valid_keys = ServiceProviderDatasResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return ServiceProviderDatasResponse(**filtered_data)

    def companyData(
        self, request: CompanyDataRequest, skip_block: bool = False
    ) -> CompanyDataResponse:
        params = asdict(request) if request else {}
        data = self.client._call("companyData", params, skip_block=skip_block)
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = CompanyDataResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CompanyDataResponse(**filtered_data)

    def quantityList(
        self, request: QuantityListRequest, skip_block: bool = False
    ) -> QuantityListResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("quantityList", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = QuantityListResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return QuantityListResponse(**filtered_data)

    def currencyDownload(
        self, request: CurrencyDownloadRequest, skip_block: bool = False
    ) -> CurrencyDownloadResponse:
        params = asdict(request) if request else {}
        if "type_" in params:
            params["type"] = params.pop("type_")
        data = self.client._call("currencyDownload", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = CurrencyDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CurrencyDownloadResponse(**filtered_data)

    def regularityDownload(
        self, request: RegularityDownloadRequest, skip_block: bool = False
    ) -> RegularityDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("regularityDownload", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        if "id" in data:
            data["id_"] = data.pop("id")
        valid_keys = RegularityDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return RegularityDownloadResponse(**filtered_data)

    def countryDownload(
        self, request: CountryDownloadRequest, skip_block: bool = False
    ) -> CountryDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("countryDownload", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = CountryDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return CountryDownloadResponse(**filtered_data)

    def postcodeDownload(
        self, request: PostcodeDownloadRequest, skip_block: bool = False
    ) -> PostcodeDownloadResponse:
        params = asdict(request) if request else {}
        data = self.client._call("postcodeDownload", params, skip_block=skip_block)
        valid_keys = PostcodeDownloadResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return PostcodeDownloadResponse(**filtered_data)

    def ping(self, request: PingRequest, skip_block: bool = False) -> PingResponse:
        params = asdict(request) if request else {}
        data = self.client._call("ping", params, skip_block=skip_block)
        valid_keys = PingResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return PingResponse(**filtered_data)

    def monitor(
        self, request: MonitorRequest, skip_block: bool = False
    ) -> MonitorResponse:
        params = asdict(request) if request else {}
        data = self.client._call("monitor", params, skip_block=skip_block)
        if "list" in data:
            data["list_"] = data.pop("list")
        valid_keys = MonitorResponse.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return MonitorResponse(**filtered_data)
