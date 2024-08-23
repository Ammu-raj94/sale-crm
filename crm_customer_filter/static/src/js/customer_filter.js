/** @odoo-module **/
import { onWillStart, useState } from "@odoo/owl";
import { listView } from '@web/views/list/list_view';
import { ListController } from "@web/views/list/list_controller";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class FilterSalesPerson extends ListController {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.state = useState({
            SalesPersons: false
        });
        onWillStart(async () => {
            this.state.SalesPersons = await this.orm.call("res.users", "search_read", [], {
                fields: ["id", "display_name"],
                domain: [
                    ['share', '=', false]
                ]
            });
        });
    }
    //Calling the default function splitAndAddDomain when changing the Customer.
    onChangePerson(ev) {
        if (ev.target.value != 'All') {
            let customer_name = ev.target.value;
            this.env.searchModel.splitAndAddDomain(`[("user_id", "ilike", '${customer_name}')]`)
        }
    }
};

export const CRMloadListView = {
    ...listView,
    Controller: FilterSalesPerson,
};
FilterSalesPerson.template = "FilterSalesPerson";
registry.category("views").add("sales_person_filter", CRMloadListView);
