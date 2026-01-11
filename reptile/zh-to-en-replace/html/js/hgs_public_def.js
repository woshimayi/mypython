const KEY_ATTR_NAME = "hgs_key";
const KEY_ATTR_SET = "hgs_set_key";
const KEY_STATIC = "hgs_static_key"
const HGS_SUBMIT_DIV_ID = "hgs_submit_div_id";
const HGS_REFRESEH_ID = "hgs_refresh_table_div_id";
const HGS_CHECKED_VALUE = "hgs_checked_value"

const KEY_ERROR_CODE = "errorCode"
const KEY_MESSAGE = "message"
const KEY_URL = "url"
const LOGIN_PAGE = "login.html"


var enable_console_log = 0;

function is_enable_console_log() {
	return enable_console_log;
}

var g_log_data = 0;
var g_log_layout = 0;
var g_log_func = 0;
var g_disable_commit = 0;
var g_hbusSimu = 0;

function IS_LOG_DATA_ENABLE() {
	return g_log_data;
}

function IS_LOG_LAYOUT_ENABLE() {
	return g_log_layout;
}

function IS_LOG_FUNC_ENABLE() {
	return g_log_func;
}

function IS_DISABLE_COMMIT() {
	return g_disable_commit;
}

function LOG_DATA(para) {
	if (g_log_data) {
		console.log(para);
	}
}

function LOG_LAYOUT(para) {
	if (g_log_layout) {
		console.log(para);
	}
}

function LOG_FUNC(para) {
	if (g_log_func) {
		console.log(para);
	}
}

function IS_HBUS_SIMU(){
    return g_hbusSimu;
}
