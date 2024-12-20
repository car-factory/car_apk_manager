{% load gwm_tags %}
{
	"code": 200,
	"message": "查询成功",
	"data": {
		"apk_version": "{{ apk.name }}/{{ apk.version }}",
		"apk_url": "{{ apk.file_url }}",
		"apk_msg": "{{ apk.describe }}{{ apk.comment }}【本服务由车友社区免费提供技术支持】",
		"isUpdate": "{{ apk.is_update|bool_to_yes_no }}",
		"apk_forceUpdate": "{{ apk.force_update|bool_to_yes_no }}",
		"notice": {
			"vin_notice": [
				"VIN码可以在仪表板左上方（前风挡玻璃后面）和车辆铭牌上获得。",
				"本应用适用于2019年及之后生产的车型。"
			],
			"add_notice": [
				"制造年月可通过车辆铭牌获得。",
				"本应用适用于2019年及之后生产的车型。"
			]
		},
		"notice_en": {
			"vin_notice": [],
			"add_notice": [
				"The date can be obtained from the certification label."
			]
		}
	}
}
