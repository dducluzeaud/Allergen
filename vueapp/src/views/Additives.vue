<template>
  <div class="container">
    <section id="additives" class="section">
      <div v-if="additives">
        <b-table
          :data="additives"
          paginated
          backend-pagination
          :total="total"
          :per-page="perPage"
          @page-change="onPageChange"
          backend-sorting
          :default-sort-direction="defaultSortOrder"
          :default-sort="[sortField, sortOrder]"
          @sort="onSort"
        >
          <template slot-scope="props">
            <b-table-column
              class="has-text-centered"
              field="risk"
              label="Risque"
              centered
              sortable
            >{{ (props.row.risk) | emojizeRisk }}</b-table-column>

            <b-table-column
              class="has-text-centered"
              field="additive_name"
              label="Additif"
              centered
              sortable
            >{{ props.row.additive_name |capitalize }}</b-table-column>

            <b-table-column field="description" label="Description">{{ props.row.description }}</b-table-column>
          </template>
        </b-table>
        <ul>
          <li>✅ Sans risque</li>
          <li>⚠️ Peu présenté des risques</li>
          <li>❓ Douteux</li>
          <li>⁉️ Présente des risques</li>
          <li>⛔️ A éviter</li>
        </ul>
      </div>
      <div v-else>
        <p>Aucun additif</p>
      </div>
    </section>
  </div>
</template>

<script>
import { APIServiceAdditives } from '@/api/APIService'

const APIAdditives = new APIServiceAdditives()

export default {
  data() {
    return {
      additives: [],
      total: 0,
      nextPage: '',
      previousPage: '',
      sortField: 'additive_name',
      sortOrder: '-',
      defaultSortOrder: '',
      page: 1,
      perPage: 20
    }
  },
  created() {
    // Fetch  the data the view is created
    // and the data is already being observed
    this.getAdditives()
  },
  watch: {
    // call again the method if the route changes
    $route: 'getAdditives'
  },
  methods: {
    getAdditives() {
      const params = [
        `ordering=${this.sortOrder}${this.sortField}`,
        `offset=${(this.page - 1) * 20}`
      ].join('&')
      this.loading = true
      APIAdditives.getAdditives(params)
        .then(data => {
          this.additives = data.results
          this.total = data.count
          this.nextPage = data.next
          this.previousPage = data.previous
        })
        .catch(error => {
          this.data = []
          this.total = 0
          this.loading = false
          throw error
        })
      this.loading = false
    },
    /*
     * Handle page-change event
     */
    onPageChange(page) {
      this.page = page
      this.getAdditives()
    },
    /*
     * Handle sort event
     */
    onSort(field, order) {
      this.sortField = field
      this.sortOrder = order === 'desc' ? '-' : ' '
      this.getAdditives()
    }
  }
}
</script>
